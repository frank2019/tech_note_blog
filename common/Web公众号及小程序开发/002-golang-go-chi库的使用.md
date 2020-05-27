go-chi的使用



# 一.go-chi 是什么

go-chi是一个golang的路由包。

类似的可以作为对别的有：   golang 语言内置有路由 即http.ServeMux，

golang 语言内置有路由 即http.ServeMux， 不过因为性能的原因，有很多路由的第三方包，他们的各自特点：

//todo



##1. http.ServeMux

ServeMux类型是HTTP请求的多路转接器。它会将每一个接收的请求的URL与一个注册模式的列表进行匹配，并调用和URL最匹配的模式的处理器。

模式是固定的、由根开始的路径，如"/favicon.ico"，或由根开始的子树，如"/images/"（注意结尾的斜杠）。较长的模式优先于较短的模式，因此如果模式"/images/"和"/images/thumbnails/"都注册了处理器，后一个处理器会用于路径以"/images/thumbnails/"开始的请求，前一个处理器会接收到其余的路径在"/images/"子树下的请求。

注意，因为以斜杠结尾的模式代表一个由根开始的子树，模式"/"会匹配所有的未被其他注册的模式匹配的路径，而不仅仅是路径"/"。

模式也能（可选地）以主机名开始，表示只匹配该主机上的路径。指定主机的模式优先于一般的模式，因此一个注册了两个模式"/codesearch"和"codesearch.google.com/"的处理器不会接管目标为"<http://www.google.com/>"的请求。

ServeMux还会注意到请求的URL路径的无害化，将任何路径中包含"."或".."元素的请求重定向到等价的没有这两种元素的URL。

### 

### 1.1 func NewServeMux() *ServeMux

NewServeMux创建并返回一个新的*ServeMux

### 1.2 func (mux *ServeMux) Handle(pattern string, handler Handler)

Handle注册HTTP处理器handler和对应的模式pattern。如果该模式已经注册有一个处理器，Handle会panic。

```
func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)
```

```
func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)
```



### 参考链接



[type ServeMux](https://studygolang.com/static/pkgdoc/pkg/net_http.htm#ServeMux)

- [func NewServeMux() *ServeMux](https://studygolang.com/static/pkgdoc/pkg/net_http.htm#NewServeMux)
- [func (mux *ServeMux) Handle(pattern string, handler Handler)](https://studygolang.com/static/pkgdoc/pkg/net_http.htm#ServeMux.Handle)
- [func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request))](https://studygolang.com/static/pkgdoc/pkg/net_http.htm#ServeMux.HandleFunc)
- [func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)](https://studygolang.com/static/pkgdoc/pkg/net_http.htm#ServeMux.Handler)
- [func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)](https://studygolang.com/static/pkgdoc/pkg/net_http.htm#ServeMux.ServeHTTP)

1. https://studygolang.com/pkgdoc



## 有哪些接口？

```
var rootMux *http.ServeMux
var WildcardRouter *wildcard_router.WildcardRouter

func Router() *http.ServeMux {
	if rootMux == nil {
		router := chi.NewRouter()

		router.Use(func(next http.Handler) http.Handler {
			return http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
				var (
					tx         = db.DB
					qorContext = &qor.Context{Request: req, Writer: w}
				)

				if locale := utils.GetLocale(qorContext); locale != "" {
					tx = tx.Set("l10n:locale", locale)
				}

				ctx := context.WithValue(req.Context(), utils.ContextDBName, publish2.PreviewByDB(tx, qorContext))
				next.ServeHTTP(w, req.WithContext(ctx))
			})
		})

		router.Get("/", controllers.HomeIndex)
		router.Get("/products", controllers.ProductIndex)
		router.Get("/products/{code}", controllers.ProductShow)
		router.Get("/g/{gender}", controllers.ProductGenderShow)
		router.Get("/category/{code}", controllers.CategoryShow)
		router.Get("/switch_locale", controllers.SwitchLocale)

		router.With(auth.Authority.Authorize()).Route("/account", func(r chi.Router) {
			r.Get("/", controllers.AccountShow)
			r.With(auth.Authority.Authorize("logged_in_half_hour")).Post("/add_user_credit", controllers.AddUserCredit)
			r.Get("/profile", controllers.ProfileShow)
			r.Post("/profile", controllers.SetUserProfile)
			r.Post("/profile/billing_address", controllers.SetBillingAddress)
			r.Post("/profile/shipping_address", controllers.SetShippingAddress)
		})

		router.Route("/cart", func(r chi.Router) {
			r.Get("/", controllers.ShowCartHandler)
			r.Get("/checkout", controllers.CheckoutCartHandler)
			// r.Post("/", controllers.AddToCartHandler)
			// r.Post("/checkout", controllers.OrderCartHandler)
			// r.Delete("/:id", controllers.RemoveFromCartHandler)
		})

		rootMux = http.NewServeMux()

		rootMux.Handle("/auth/", auth.Auth.NewServeMux())
		rootMux.Handle("/system/", utils.FileServer(http.Dir(filepath.Join(config.Root, "public"))))
		assetFS := bindatafs.AssetFS.FileServer(http.Dir("public"), "javascripts", "stylesheets", "images", "dist", "fonts", "vendors")
		for _, path := range []string{"javascripts", "stylesheets", "images", "dist", "fonts", "vendors"} {
			rootMux.Handle(fmt.Sprintf("/%s/", path), assetFS)
		}

		WildcardRouter = wildcard_router.New()
		WildcardRouter.MountTo("/", rootMux)
		WildcardRouter.AddHandler(router)
	}
	return rootMux
}
```









## 参考链接

1. [go-chi on github](https://github.com/go-chi/chi)

