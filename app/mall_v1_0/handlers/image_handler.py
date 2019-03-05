# coding: utf-8

from flask import request
from flask_restful import Resource
from ..models import Image
from app import db
from ..utils.tools import retJsonData
from flask import current_app as app
from os import path
from werkzeug.utils import secure_filename
from datetime import datetime


class UploadImage(Resource):
    '''
    上传图片 存放到指定路径
    '''
    def post(self):
        try:
            f = request.files['file']
            basepath = path.abspath(path.dirname(__file__))
            upload_path = path.join(basepath, 'uplaod_images')
            filename = datetime.now().strftime('%Y%m%d%H%M%S') + '_' + secure_filename(f.filename)
            f.save(upload_path, filename)
            img = Image(name=filename)
            db.session.add(img)
            db.session.flush()
            db.session.commit()
            return retJsonData(repcd='0000', msg='上传成功', param={'img_id': img.id, 'filename': filename})
        except KeyError as e:
            app.logger.exception(e)
        except BaseException as e:
            db.session.rollback()
            app.logger.exception(e)
