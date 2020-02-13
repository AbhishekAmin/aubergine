from celery.decorators import task
from celery.utils.log import get_task_logger

from .serializers import ImagesSerializer



logger = get_task_logger(__name__)


@task(name="add_image_urls_task")
def add_image_urls_task(data, user):
    try:
        logger.info("Image URLs added.")
        region_name = "ap-south-1"
        bucket_name = "aubergine-static"

        keys = data["keys"]

        image_data = {}
        image_data['author'] = user

        for key in keys:
            image_data['image_url'] = "https://%s.s3.%s.amazonaws.com/%s" % (bucket_name, region_name, key)

            serializer = ImagesSerializer(data=image_data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

        return "Images added."

    except Exception as e:
        print(2, str(e))
        return str(e)