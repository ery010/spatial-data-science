# Practice Quiz 1
*Instructions: Check the Appropriate Options*

from IPython.display import HTML
import random

def hide_toggle(for_next=False):
    this_cell = """$('div.cell.code_cell.rendered.selected')"""
    next_cell = this_cell + '.next()'

    toggle_text = ''  # text shown on toggle link
    target_cell = this_cell  # target cell to control with toggle
    js_hide_current = ''  # bit of JS to permanently hide code in current cell (only when toggling next cell)

    if for_next:
        target_cell = next_cell
        toggle_text += ' next cell'
        js_hide_current = this_cell + '.find("div.input").hide();'

    js_f_name = 'code_toggle_{}'.format(str(random.randint(1,2**64)))

    html = """
        <script>
            function {f_name}() {{
                {cell_selector}.find('div.input').toggle();
            }}

            {js_hide_current}
        </script>

        <a href="javascript:{f_name}()">{toggle_text}</a>
    """.format(
        f_name=js_f_name,
        cell_selector=target_cell,
        js_hide_current=js_hide_current, 
        toggle_text=toggle_text
    )

    return HTML(html)

import ipywidgets as widgets
from IPython.display import display, Markdown

question1 = widgets.Label('1. ______ is the statistic used to quantify the degree of spatial autocorrelation in spatial statistics.')
radio1 = widgets.RadioButtons(
    options=["Moran's I", 'R-value', 'Autocorrelation R', 'None of the Above'],
    layout={'width': 'max-content'}, # If the items' names are long,
    disabled=False,
    value = 'None of the Above'
)


question2 = widgets.Label('2. Which of the following is the full form of EPSG?')
radio2 = widgets.RadioButtons(
    options=["European Spatial Group", 'European Petroleum Survey Group', 'Earth Position Survery Group', 'None of the Above'],
    layout={'width': 'max-content'}, # If the items' names are long,
    disabled=False,
    value = 'None of the Above'
)


question3 = widgets.Label('3. Which of the following are valid components of shapefiles?')
shp = widgets.Checkbox(
    value=False,
    description='.shp',
    disabled=False,
    indent=False
)
shx = widgets.Checkbox(
    value=False,
    description='.shx',
    disabled=False,
    indent=False
)
dbf = widgets.Checkbox(
    value=False,
    description='.dbf',
    disabled=False,
    indent=False
)
prj = widgets.Checkbox(
    value=False,
    description='.prj',
    disabled=False,
    indent=False
)

all_above_q3 = widgets.Checkbox(
    value=False,
    description='All of the Above',
    disabled=False,
    indent=False, 
    layout={'width': 'max-content'},
)

output = widgets.Output()
evaluate = widgets.Button(
    description='Evaluate',
    disabled=False,
    button_style='info', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Evaluate',
    icon='check', # (FontAwesome names without the `fa-` prefix), 
)
reset = widgets.Button(
    description='Reset',
    disabled=False,
    button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Reset',
    icon='repeat', # (FontAwesome names without the `fa-` prefix), 
)

def reset_btn(b):
    radio1.disabled = False
    radio2.disabled = False
    shp.disabled = False
    shx.disabled = False
    dbf.disabled = False
    prj.disabled = False
    all_above_q3.disabled = False
    output.clear_output()

def eval_quiz(b):
    output.clear_output()
    results = 'RESULTS\n\n'
    cond_chk = False
    with output:
        radio1.disabled = True
        radio2.disabled = True
        shp.disabled = True
        shx.disabled = True
        dbf.disabled = True
        prj.disabled = True
        all_above_q3.disabled = True
        
        
        output.clear_output()
        if radio1.value == "Moran's I":
            results +='Question 1: ✔\n'
        else:
            results +="Question 1: ✘ (Moran's I)\n"
            
            
        if radio2.value == "European Petroleum Survey Group":
            results +='Question 2: ✔\n'
        else:
            results +="Question 2: ✘ (European Petroleum Survey Group)\n"
            
        if shp.value == True and shx.value == True and dbf.value == True and prj.value == True:
            cond_chk = True
            results +='Question 3: ✔\n'
            
        elif all_above_q3.value == True and not cond_chk:
            results +='Question 3: ✔\n'
        
        else:
            results +='Question 3: ✘ (All of the Above)\n'
            
            
            
        
            
    print(results)
        
        
evaluate.on_click(eval_quiz)
reset.on_click(reset_btn)

display(question1)
display(radio1)

display(question2)
display(radio2)

display(question3)
display(shp)
display(shx)
display(dbf)
display(prj)
display(all_above_q3)

display(evaluate)
display(reset)
display(output)

#hide_toggle()



