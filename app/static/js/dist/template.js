!function(e){"use strict";function t(){this.defaultTemplate='<li data-id="{{id}}" class="{{completed}}"><div class="view"><input class="toggle" type="checkbox" {{checked}}><label>{{title}}</label><button class="destroy"></button></div></li>'}var l={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#x27;","`":"&#x60;"},o=function(e){return l[e]},c=/[&<>"'`]/g,r=new RegExp(c.source),p=function(e){return e&&r.test(e)?e.replace(c,o):e};t.prototype.show=function(e){var t,l,o="";for(t=0,l=e.length;t<l;t++){var c=this.defaultTemplate,r="",n="";e[t].completed&&(r="completed",n="checked"),c=c.replace("{{id}}",e[t].id),c=c.replace("{{title}}",p(e[t].title)),c=c.replace("{{completed}}",r),c=c.replace("{{checked}}",n),o+=c}return o},t.prototype.itemCounter=function(e){var t=1===e?"":"s";return"<strong>"+e+"</strong> item"+t+" left"},t.prototype.clearCompletedButton=function(e){return e>0?"Clear completed":""},e.app=e.app||{},e.app.Template=t}(window);