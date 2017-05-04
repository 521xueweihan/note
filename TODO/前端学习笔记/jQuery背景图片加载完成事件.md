```html
<script type="text/javascript" src="http://catmull.uk/downloads/bg-loaded/bg-loaded.js"></script>
<script type="text/javascript">
   $('body').bgLoaded({
      afterLoaded : function() {
         alert('Background image done loading');
      }
   });
</script>
```

参考：
- [stackoverflow](http://stackoverflow.com/questions/5057990/how-can-i-check-if-a-background-image-is-loaded)
