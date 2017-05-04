```javascript
function delete_post(article_id, title) {
    if(confirm("确认删除“"+title+"”吗？")){
        $.ajax({
            type:'POST',
            url: '/article/delete/' + article_id,
            success:function(data) {
               alert('删除成功！');
               window.location.href = '/article/list';
            },
            error:function(data){
               console.log(data);
               alert('删除出错！');
               window.location.reload();
            }
        });
    }
}
```
