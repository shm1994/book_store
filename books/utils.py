# books/utils.py
import jdatetime
from datetime import datetime


def convert_to_jalali_str(gregorian_datetime, format_string="%Y/%m/%d ساعت %H:%M"):
    """
    تبدیل یک شیء datetime میلادی به رشته تاریخ شمسی با فرمت دلخواه.
    اگر ورودی None یا نامعتبر باشد، پیام مناسبی برمی‌گرداند.
    """
    if gregorian_datetime is None:
        return "تاریخ ثبت نشده"

    # مطمئن شو که ورودی از نوع datetime است و timezone را حذف کن
    if isinstance(gregorian_datetime, datetime):
        try:
            # اگر تاریخ Aware است، Naive کن. برای jdatetime ساده‌تر است.
            naive_datetime = gregorian_datetime.replace(tzinfo=None)
        except AttributeError:
            naive_datetime = gregorian_datetime  # اگر از قبل Naive بود
    else:
        # اگر نوع ورودی اشتباه بود
        return "تاریخ نامعتبر"

    try:
        jalali_dt = jdatetime.datetime.fromgregorian(datetime=naive_datetime)
        return jalali_dt.strftime(format_string)
    except Exception as e:
        # برای دیباگ کردن خطاها
        print(f"Error converting date to Jalali: {e}")
        return "خطای تبدیل تاریخ"
