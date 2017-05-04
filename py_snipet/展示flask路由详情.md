## 展示 flask 路由详情
I make a helper method on my `manage.py`:
```python
@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line
```

The output looks like:
```
CampaignView:edit              HEAD,OPTIONS,GET     /account/[account_id]/campaigns/[campaign_id]/edit
CampaignView:get               HEAD,OPTIONS,GET     /account/[account_id]/campaign/[campaign_id]
CampaignView:new               HEAD,OPTIONS,GET     /account/[account_id]/new

```

I make a helper method on my `manage.py`:

For more on manage.py checkout: http://flask-script.readthedocs.org/en/latest/

## 参考
- [flask snippets](http://flask.pocoo.org/snippets/117/)
