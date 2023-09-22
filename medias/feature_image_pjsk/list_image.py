import os
image_list=os.listdir()
for now_image in image_list:
    if now_image.endswith(".webp"):
        print("- /medias/feature_image_pjsk/"+now_image)
