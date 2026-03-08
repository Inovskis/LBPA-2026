def get_slide(number):
    """Return the render function for the given slide number (1-17)."""
    if number == 1:
        from slides.slide_01_title import render
    elif number == 2:
        from slides.slide_02_new_era import render
    elif number == 3:
        from slides.slide_03_problem import render
    elif number == 4:
        from slides.slide_04_solution import render
    elif number == 5:
        from slides.slide_05_demo import render
    elif number == 6:
        from slides.slide_06_why_python import render
    elif number == 7:
        from slides.slide_07_python_libs import render
    elif number == 8:
        from slides.slide_08_ai_assistant import render
    elif number == 9:
        from slides.slide_09_ai_examples import render
    elif number == 10:
        from slides.slide_10_prediction import render
    elif number == 11:
        from slides.slide_11_ralph_wiggum import render
    elif number == 12:
        from slides.slide_12_deployment import render
    elif number == 13:
        from slides.slide_13_other_tools import render
    elif number == 14:
        from slides.slide_14_pyrevit import render
    elif number == 15:
        from slides.slide_15_podcasts import render
    elif number == 16:
        from slides.slide_16_universities import render
    elif number == 17:
        from slides.slide_17_summary import render
    else:
        raise ValueError(f"Invalid slide number: {number}")
    return render
