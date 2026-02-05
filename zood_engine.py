import requests
import os

# هذي المفاتيح بنحطها في إعدادات الأمان بعد شوي
BLOG_ID = os.getenv('BLOG_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def post_to_zood():
    # عنوان المنشور ومحتواه
    title = "🚀 انطلاق منصة ذود العالمية"
    content = "تم تشغيل نظام النشر الآلي بنجاح. منصة ذود لخدمات الإبل والحلال بدأت العمل الآن."
    
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "title": title,
        "content": content
    }
    
    # محاولة النشر
    r = requests.post(url, json=payload, headers=headers)
    
    if r.status_code == 200:
        print("✅ مبروك! البوت نشر أول موضوع في الموقع.")
    else:
        print(f"❌ فيه مشكلة في الصلاحيات: {r.text}")

if __name__ == "__main__":
    post_to_zood()
