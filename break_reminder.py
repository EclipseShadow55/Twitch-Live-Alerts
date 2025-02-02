from twitchio.ext import commands
import asyncio
import twitch_access as ta


class Bot(commands.Bot):

    def __init__(self, token, prefix, initial_channels, interval, checkpoints):
        super().__init__(token=token, prefix=prefix, initial_channels=initial_channels, nick='BreakReminderBot', )
        self.interval = interval
        self.checkpoints = checkpoints
        self.iteration_counter = 1
        self.counter = 0
        self.snooze_time = 0
        self.break_time = 0
        self.stop_flag = False

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        asyncio.create_task(self.count_minutes())

    async def event_message(self, message):
        if message.echo:
            return

        await self.handle_commands(message)

    async def count_minutes(self):
        while not self.stop_flag:
            if self.snooze_time > 0:
                await asyncio.sleep(self.snooze_time * 60)
                self.snooze_time = 0
            elif self.break_time > 0:
                await asyncio.sleep(self.break_time * 60)
                self.break_time = 0
                self.counter = 0
            else:
                await asyncio.sleep(60)
                self.counter += 1
                if self.counter in [self.interval - cp for cp in self.checkpoints]:
                    checkpoint = self.interval - self.counter
                    await self.send_message(f"The stream is {checkpoint} minutes away from break time #{self.iteration_counter}")
                if self.counter >= self.interval:
                    await self.send_message(f"Break time #{self.iteration_counter} reached. Take a break.")
                    self.counter = 0
                    self.iteration_counter += 1

    async def send_message(self, message):
        for channel in self.connected_channels:
            await channel.send(message)

    @commands.command(name='snooze')
    async def snooze_command(self, ctx, length: int = 15):
        if ctx.author.is_mod or ctx.author.name == self.nick:
            self.snooze_time = length
            await ctx.send(f'{ctx.author.name}, snooze command received for {length} minutes!')

    @commands.command(name='break')
    async def break_command(self, ctx, length: int = 15):
        if ctx.author.is_mod or ctx.author.name == self.nick:
            self.break_time = length
            self.counter = 0
            await ctx.send(f'{ctx.author.name}, break command received for {length} minutes!')

    async def stop_bot(self):
        self.stop_flag = True
        await self.close()


def start_bot(token, channel, interval, checkpoints):
    bot = Bot(token=token, prefix='!', initial_channels=[channel], interval=interval, checkpoints=checkpoints)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start())
    return bot


def stop_bot(bot):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.stop_bot())


def main(client_id, client_secret, channel, interval, checkpoints):
    token = ta.get_access_token(client_id, client_secret)
    bot = start_bot(token, channel, interval, checkpoints)
    return bot
