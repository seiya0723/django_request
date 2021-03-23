from django.shortcuts import render,redirect

from django.views import View


BOOKS_DATA  = [ { "id":1,"title":"HTML+CSS本","price":2000 },
                { "id":2,"title":"jQuery本",  "price":2500 },
                { "id":3,"title":"Django本",  "price":3000 },
                ]

class IndexView(View):

    def get(self, request, *args, **kwargs):

        books   = BOOKS_DATA
        #books   = []

        context = { "books":books }
        
        return render(request,"hello/index.html",context)

    def post(self, request, *args, **kwargs):

        if "id" in request.POST:
            print( "ID:" , request.POST["id"] ," を買いました")


        #トップページにリダイレクトする。urls.pyで定義したnameを元にURLを逆引きしてリダイレクト
        # POST文ではrender関数を実行して表示させるのではなく、任意のページにリダイレクトする。(誤って再送信を防ぐため)
        return redirect("hello:index")


index   = IndexView.as_view()


