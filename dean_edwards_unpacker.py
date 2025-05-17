# Most other implementations that directly copy DEs packer have a bunch of unecessary stuff, wrote this for my web-reversing guide
import re

def unpack(packed_js):
  matched_data = re.search(r"}\('(.+)',(\d+),\d+,'(.+)'\.split", packed_js)
  if not matched_data:
    return None

  psuedocode = matched_data.group(1)
  base = int(matched_data.group(2))
  variables = matched_data.group(3).split("|")

  def replace_match(match):
    token = match.group(1)
    num = int(token, base)
    return variables[num] or token

  unpacked_js = re.sub(r'(\w+)', replace_match, psuedocode)
  return unpacked_js

if __name__ == "__main__":
  packed_input = """eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0 i="9";0 3="e";0 1="a";0 2="b";0 4=", ";0 5="c";0 6="f";0 7="d";0 8="!";g.h(i+3+1+1+2+4+5+2+6+1+7+8)',19,19,'var|iii|iiii|ii|iiiii|iiiiii|iiiiiii|iiiiiiii|iiiiiiiii|H|l|o|W|||r|console|log|'.split('|'),0,{}))"""
  unpacked_output = unpack(packed_input)
  print(unpacked_output)
