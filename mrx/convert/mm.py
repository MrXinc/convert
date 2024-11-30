import os
import sys
import csv
import inspect
from mako.template import Template


this_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def get_csv(feed, comment="#"):
    """ read csv file, skipping any line that begins with a comment (default to '#') """
    csv_data = []
    with open(feed, 'r') as fp:
        for c in fp:
            print(c)
    return csv_data


def render_template(tmpl, csv_dict, do_print=False):
    def safe_num(num, def_num=888):
        ret_val = def_num
        try:
            ret_val = int(num)
        except:
            ret_val = def_num
        return ret_val

    loader_tmpl = Template(filename=os.path.join(this_module_dir, 'tmpl', tmpl))
    ret_val = loader_tmpl.render(csv=csv_dict, agency=make_feed_agency_id, img=make_logo, num=safe_num)
    if do_print:
        print(ret_val)
    else:
        txt = tmpl.replace('mako', 'txt')
        print("output:  " + txt)
        #file_utils.cat(tmpl.replace('mako', 'txt'), input=ret_val)
        with open(txt, "w+") as f:
            f.write(ret_val)
    return ret_val


def txt2mm():
    """
    csv2json: simple example showing convert to pretty json (array)
    > poetry run csv2json  # default file is ott/convert/csv2json/feeds.csv
    > poetry run csv2json ott/convert/csv2json/logos.csv
    """
    import json
    args = sys.argv[1:]
    file = args[0] if len(args) > 0 else os.path.join(this_module_dir, "test.txt")
    csv = get_csv(file)
    print(json.dumps(csv, indent=4))
