<map>
<node TEXT="${date_time}">
%for l in lines:
  %if l['text'].strip():
  %if l['terminate']:
  <node TEXT="${l['text']}" POSITION="right"></node>
  %else
  <node TEXT="${l['text']}" POSITION="right">
  %endif
  %elif l['terminate']:
  </node>
  %endif
%endfor
</node>
</map>
