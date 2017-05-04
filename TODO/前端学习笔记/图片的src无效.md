```html
<img src="{{ ic.logo_url|fit_url_security or static_url('img/logo.png') }}"onError="this.src='{{ static_url('img/logo.png') }}';"  class="ic-logo">
```

onError属性就是在有错误时，对这个标签下的src重新赋值。
