## معرفی:
این اسکریپت با پایتون و سلنیوم نوشته شده و به طور خودکار از طریق مرورگر گوگل کروم وارد حساب کاربری دانشجو شده و تمام کلاسهای ضبط شده قابل دانلود ترم جاری رو به صورت پوشه بندی شده دانلود میکنه

## راه‌اندازی:
۱. کامپایلر پایتون و مرورگر گوگل کروم روی سیستم نصب باشه

۲.  پکیچهای زیر رو با کامندهای زیر توی محیطCmd نصب کنید:

	pip install selenium==4.29.0

	pip install webdriver-manager==4.0.2


۳. در فایل user-pass.txt یوز و پسورد سامانه sess تون رو بعد از دو نقطه بنویسید.

۴. قبل از اجرای اسکریپت وارد سامانه سس بشید، اگه آموزش یا اساتید پیامی فرستادن پیامها رو تایید کنید که وقتی اسکریپت وارد سامانه میشه به پیام ها برنجوره وگرنه خطا میده و متوقف میشه.

۵. حالا فایل OfflineVUS.py رو اجرا کنید. این فایل رو هرجا اجرا کنید پوشه‌ها و فایلهای دانلودی رو همون جا میسازه

## نکات:
- این کد خودش فایلها رو پوشه‌بندی میکنه و هربار که اجرا میکنید میره از پوشه هایی که ساخته چک میکنه که کدوم فایل ها رو دانلود کرده تا دوباره دانلودشون نکنه، پس پوشه‌ها و فایلهای دانلودی رو جابه جا نکنید.
- ممکنه لود شدن مرورگر چند دقیقه طول بکشه پس صبور باشید!
- گاهی ممکنه یک فایل ناقص دانلود بشه، اون فایل رو حذف کنید و مجدد اسکریپ رو اجرا کنید که دوباره دانلود کنه