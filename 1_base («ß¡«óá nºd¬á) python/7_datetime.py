import datetime

time1 = datetime.datetime.now()  # def __str__(self): 2022-09-08 21:34:33.725308
print(time1)
print(type(time1))

print(str(time1))
print(str(time1).split(' ')[1])
print(str(time1).split(' ')[1].split('.')[0])

print(time1.strftime("%Y-%m-%d %H:%M:%S.%f"))
print(time1.strftime("%Y/%m/%dT%H:%M:%S"))

print(time1+datetime.timedelta(minutes=10))















class DateTimeUtils:
    @staticmethod
    def sleep(multiply=1.0, stop=0):
        multiply = multiply / 2
        if stop:
            time.sleep(multiply)
        else:
            time.sleep(round(random.uniform(multiply, stop), 2))

    @staticmethod
    def get_current_datetime():
        return f"{time.strftime('%Y-%m-%d %H:%M:%S')}"

    @staticmethod
    def get_current_date():
        return f"{time.strftime('%Y-%m-%d')}"

    @staticmethod
    def get_current_time():
        return f"{time.strftime('%H:%M:%S')}"

    @staticmethod
    def get_difference_datetime(days=0.0, hours=0.0, minutes=0.0, seconds=0.0):
        value = datetime.datetime.now() + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return value.replace(tzinfo=datetime.timezone.utc)

    class Example:
        @staticmethod
        def example_get_datetime():
            print(DateTimeUtils.get_current_datetime())

        @staticmethod
        def example_get_difference_datetime():
            print(DateTimeUtils.get_difference_datetime(hours=-2))