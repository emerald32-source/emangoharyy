import os
from PIL import Image

def fix_images():
    # 1. البحث عن ملف الأغنية وتعديل اسمها وامتدادها إلى music.mp3
    audio_exts = ('.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac', '.wma', '.mp4', '.m4p')
    audio_found = False
    
    for f in os.listdir('.'):
        f_lower = f.lower()
        # بندور على أي ملف صوتي ميكونش اسمه music.mp3 أو background.mp3 عشان نغيره
        if f_lower.endswith(audio_exts) and f_lower not in ['music.mp3', 'background.mp3']:
            try:
                os.rename(f, 'music.mp3')
                print(f"✅ تم العثور على الأغنية ({f}) وتحويل اسمها وامتدادها إلى music.mp3")
                audio_found = True
                break  # بناخد أول ملف صوتي يقابلنا بس ونكتفي بيه
            except Exception as e:
                print(f"❌ خطأ في تغيير اسم ملف الأغنية: {e}")
                
    if not audio_found:
        if os.path.exists('music.mp3'):
            print("ℹ️ ملف music.mp3 موجود بالفعل وجاهز من الأول.")
        else:
            print("⚠️ لم يتم العثور على أي ملف صوتي جديد لتسميته music.mp3")

    # 2. فلترة وترتيب صور العميل
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp', '.heic', '.jfif')
    # الصور اللي السكريبت هيعمل نفسه مش شايفها
    ignored_files = ['cake.jpg', 'loading.jpg'] 
    
    # فلترة الصور: هناخد بس الصور اللي مش في قائمة التجاهل ومش متسمية جاهز
    files = []
    for f in os.listdir('.'):
        f_lower = f.lower()
        if f_lower.endswith(valid_exts):
            if f_lower not in ignored_files and not f_lower.startswith('photo') and not f_lower.startswith('gannah'):
                files.append(f)
    
    if not files:
        print("مفيش صور جديدة للعميل محتاجة تظبيط!")
        return

    print(f"لقيت {len(files)} صورة.. هفرمتهم وأنضف الفولدر...")

    # ترتيب الصور أبجدياً
    files.sort()

    # 3. تظبيط صورة البروفايل (أول صورة في الترتيب)
    profile_src = files[0]
    try:
        with Image.open(profile_src) as img:
            img.convert('RGB').save('gannah.jpg', 'JPEG', quality=85)
        os.remove(profile_src) # مسح الأصل العشوائي
        print(f"✅ تم تجهيز gannah.jpg ومسح الأصل")
    except Exception as e:
        print(f"❌ خطأ في صورة البروفايل: {e}")

    # 4. تظبيط باقي صور البلالين بالترتيب التسلسلي
    counter = 1
    for f in files[1:]:
        try:
            with Image.open(f) as img:
                new_name = f'photo{counter}.jpg'
                img.convert('RGB').save(new_name, 'JPEG', quality=85)
            os.remove(f) # مسح الأصل العشوائي
            print(f"✅ تم تجهيز {new_name} ومسح الأصل")
            counter += 1
        except Exception as e:
            print(f"❌ خطأ في الصورة {f}: {e}")

    print("🎉 النضافة تمت بالملي! الصور والأغنية جاهزين والملفات العشوائية اتمسحت.")

if __name__ == "__main__":
    fix_images()