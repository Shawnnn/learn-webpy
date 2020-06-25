import web

render = web.template.render('templates/') #使用模板

urls = (
    #'/(.*)', 'index'  #不好的用法
    '/', 'index' 

) # 当访问根目录时候，用index类去处理

class index:
    def GET(self):
        #name = 'Neo' #程序定义好参数
        data = web.input(name=None)
        return render.index(data.name) # 函数名字和你在模板文件的名字一致
        # return render.index(name)

if __name__ == '__main__':
    app = web.application(urls,globals())
    app.run()