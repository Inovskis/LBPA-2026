def get_slide(number):
    """Return the render function for the given slide number (1-20)."""
    if number == 1:
        from slides.slide_01_title import render
    elif number == 2:
        from slides.slide_02_history_origins import render
    elif number == 3:
        from slides.slide_03_history_deep_learning import render
    elif number == 4:
        from slides.slide_04_history_llm import render
    elif number == 5:
        from slides.slide_05_paradigm import render
    elif number == 6:
        from slides.slide_06_problem import render
    elif number == 7:
        from slides.slide_07_example import render
    elif number == 8:
        from slides.slide_08_demo import render
    elif number == 9:
        from slides.slide_09_why_python import render
    elif number == 10:
        from slides.slide_10_python_libs import render
    elif number == 11:
        from slides.slide_11_ai_assistant import render
    elif number == 12:
        from slides.slide_12_ai_examples import render
    elif number == 13:
        from slides.slide_13_prediction import render
    elif number == 14:
        from slides.slide_14_ralph_wiggum import render
    elif number == 15:
        from slides.slide_15_deployment import render
    elif number == 16:
        from slides.slide_16_other_tools import render
    elif number == 17:
        from slides.slide_17_pyrevit import render
    elif number == 18:
        from slides.slide_18_podcasts import render
    elif number == 19:
        from slides.slide_19_universities import render
    elif number == 20:
        from slides.slide_20_summary import render
    else:
        raise ValueError(f"Invalid slide number: {number}")
    return render
