import jdatetime
from django import template

register = template.Library()

PERSIAN_MONTHS = [
    "فروردین", "اردیبهشت", "خرداد",
    "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر",
    "دی", "بهمن", "اسفند"
]

PERSIAN_DIGITS = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}


def to_persian_numbers(s):
    return "".join(PERSIAN_DIGITS.get(ch, ch) for ch in str(s))


@register.filter
def jalali_datetime(value):
    """
    خروجی نمونه:
    ۲۱ آبان ۱۴۰۳، ساعت ۱۸:۴۰
    """
    if not value:
        return ""

    j = jdatetime.datetime.fromgregorian(datetime=value)

    day = to_persian_numbers(j.day)
    month = PERSIAN_MONTHS[j.month - 1]
    year = to_persian_numbers(j.year)

    hour = to_persian_numbers(str(j.hour).zfill(2))
    minute = to_persian_numbers(str(j.minute).zfill(2))

    return f"{day} {month} {year}، ساعت {hour}:{minute}"
