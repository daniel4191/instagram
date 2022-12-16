# 이건 정규표현식을 계속 쓰는 번거로움을 제거하기 위한 클래스다.
class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        # return "%04d" % value
        return str(value)


class MonthConverter(YearConverter):
    regex = r"\d{1,2}"


class DayConverter(YearConverter):
    regex = r"[0123]\d"