# -*- coding: utf-8 -*-

from loginboard.loginboard_blueprint import loginboard
from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user
from loginboard.database import dao
from loginboard.model.post import Post
from wtforms import Form, StringField, validators, HiddenField, TextAreaField


# 게시물 작성 폼
class PostForm(Form):
    #제목
    title = \
        StringField('Title',
                    [validators.DataRequired(u'제목은 필수사항입니다'),
                     validators.Length(
                         min=1,
                         max=100,
                         message=u'100글자가 최대입니다.'
                     )])
    #내용
    content = \
        TextAreaField('Content',
                    [validators.DataRequired(u'내용은 필수사항입니다'),
                     validators.Length(
                         min=1,
                         max=100,
                         message=u'100글자가 최대입니다.'
                     )])


@loginboard.route('/board', methods=['GET'])
@login_required
def board():
    # db긁어서 전체를 읽어온다음 해당 객체를 전달해줌
    posts = dao.query(Post).\
        order_by(Post.upload_date.desc()).\
        all()
    return render_template('board.html', posts=posts)

# 글쓰기
@loginboard.route('/board/write', methods=['GET', 'POST'])
@login_required
def board_write():
    form = PostForm(request.form)
    if request.method == 'GET':
        return render_template('write_form.html',
                               form=form)

    #post
    if form.validate():
        try:
            post = Post(current_user.id, form.title.data, form.content.data,  datetime.today())
            dao.add(post)
            dao.commit()
        except Exception as e:
            dao.rollback()
            raise e
        return redirect(url_for('loginboard.board'))
    else:
        return redirect(url_for('loginboard.board_write'))