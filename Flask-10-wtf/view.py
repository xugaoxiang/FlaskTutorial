class RegView(MethodView):
    def get(self):
        form = UserRegisterForm(request.form)
        return render_template('register.html', form=form)

    def post(self):
        form = UserRegisterForm(request.form)
        if User.query.filter_by(username=form.username.data).first():
            flash("当前用户名已经注册！")
            return render_template('register.html', form=form)
        elif User.query.filter_by(email=form.email.data).first():
            flash("当前邮箱已经注册！")
            return render_template('register.html', form=form)
        else:
            form.validate_on_submit()
            user = User(
                form.username.data,
                form.password.data,
                form.email.data,
            )
            user.save()
            return redirect(url_for('.login'))