from manimlib import *
import numpy as np


class Test(Scene):
    def construct(self):
        L = 2
        dot = Dot(color=RED)
        print(dot.get_center()[0])
        dot1 = always_redraw(lambda: Dot().move_to([0, np.sqrt(L ** 2 - (dot.get_center()[0]) ** 2), 0]))
        self.play(ShowCreation(dot), Write(dot1))
        # Notice that the brace and label track with the square
        self.play(dot.animate.move_to([L, 0, 0]), rate_func=there_and_back, run_time=4, )
        self.wait()

        # In general, you can alway call Mobject.add_updater, and pass in
        # a function that you want to be called on every frame.  The function
        # should take in either one argument, the mobject, or two arguments,
        # the mobject and the amount of time since the last frame.
        self.wait(4)


class Introduction(Scene):
    def construct(self):
        hello = TexText("Hello")
        name = TexText("FilipeLQJ").move_to(DOWN)
        intro = VGroup(hello, name)
        problem = TexText("The Ladder Problem")
        self.play(Write(intro))
        self.play(FadeOut(intro[0]))
        self.play(Transform(intro[1], problem))
        self.wait(4)


class ProblemDescription(Scene):
    def construct(self):
        Yellow = "#F9F871"
        Green = "#65FBD2"
        Green_discrete = "#D3FBD8"
        Blue = "#00C6CF"
        Purple = "#8083FF"

        textc_dic = {"ladder": RED, "floor": Blue, "wall": Yellow, "velocity": Green}

        scenario = Text(r"A ladder is leaned against a wall.", font="Consolas", font_size=24, t2c=textc_dic)
        condition1 = Text(r"The bottom of the ladder, which is on the floor...", font_size=24, t2c=textc_dic)
        condition2 = Text(r"...is pulled away from the wall with constant velocity.", font_size=24, t2c=textc_dic)
        constrains1 = Text(r"The ends of the ladder are constrained to the wall and floor.", font_size=24, t2c=textc_dic)
        question = Text(r"At what velocity the top of the ladder hits the floor?", font_size=28, t2c=textc_dic)

        self.play(Write(scenario))
        self.wait(2)
        self.play(scenario.animate.shift(UP), Write(condition1))
        self.wait(2)
        self.play(FadeOut(scenario), condition1.animate.shift(UP), Write(condition2))
        self.wait(2)
        self.play(FadeOut(condition1), condition2.animate.shift(UP), Write(constrains1))
        self.wait(2)
        self.play(FadeOut(condition2), constrains1.animate.shift(UP), Write(question))
        self.wait(2)
        self.play(FadeOut(constrains1))
        self.wait(2)
        self.play(FadeOut(question))
        self.wait()


class Ladder(Scene):
    def construct(self):
        Yellow = "#F9F871"
        Green = "#65FBD2"
        Green_discrete = "#D3FBD8"
        Blue = "#00C6CF"
        Purple = "#8083FF"

        intro = Text(r"Some geometry", font="Consolas", font_size=24, t2c={"geometry": Green_discrete})
        self.play(Write(intro))
        self.wait()

        # write down axes.

        axes = Axes(  # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(0, 7, 1),  # y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(0, 7, 1),  # The axes will be stretched so as to match the specified
            # height and width
            height=5, width=5,  # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={"stroke_color": GREY_A, "stroke_width": 2, },  # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={"include_tip": False, }, x_axis_config={"include_tip": False, })
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(font_size=16, num_decimal_places=1, )

        # Create axes and move intro

        self.play(Write(axes, lag_ratio=0.01, run_time=3), intro.animate.shift(3 * UP))

        # write point A then point B then create a line between them. Add always redraw on Dot_A and we fix this shit!
        L = 5
        L_axis = np.linalg.norm(axes.c2p(0, L))
        xB_initial = 3
        dot_A_static = Dot(color=Yellow).move_to(axes.c2p(0, np.sqrt(L ** 2 - xB_initial ** 2)))  # Static point created for creation animation only.
        dot_B = Dot(color=Blue).move_to(axes.c2p(xB_initial, 0))
        print(dot_B.get_center)

        def get_y(dot):
            x = axes.p2c(dot.get_center())[0]
            y = np.sqrt(L ** 2 - x ** 2)
            return y

        line_static = Line(dot_A_static, dot_B, color=RED)  # Static line created for creation animation only.

        self.play(ShowCreation(dot_B))
        self.play(ShowCreation(dot_A_static))

        self.wait()
        self.play(Write(line_static))
        dot_A = always_redraw(lambda: Dot(color=Yellow).move_to(axes.c2p(0, get_y(dot_B))))
        line_update = always_redraw(lambda: Line(dot_B, dot_A, color=RED))
        dot_origin = Dot().move_to(axes.c2p(0, 0))
        self.add(line_update, dot_A)
        self.remove(line_static, dot_A_static)

        A_static = TexText("A").next_to(dot_A,RIGHT).set_color(Yellow)
        B_static = TexText("B").next_to(dot_B,UP).set_color(Blue)

        A = always_redraw(lambda: TexText("A").next_to(dot_A,(RIGHT)).set_color(Yellow))
        B = always_redraw(lambda: TexText("B").next_to(dot_B,UP).set_color(Blue))

        # add labels and brackets to
        bx_static = Brace(Line(dot_B, dot_origin), direction=DOWN, buff=0.5)
        by_static = Brace(Line(dot_A, dot_origin), direction=LEFT, buff=0.55)
        bx_text_static = bx_static.get_text("x(t)")
        by_text_static = by_static.get_text("y(t)")

        bx = always_redraw(lambda: Brace(Line(dot_B, dot_origin), direction=DOWN, buff=0.5))
        by = always_redraw(lambda: Brace(Line(dot_A, dot_origin), direction=LEFT, buff=0.55))
        bx_text = always_redraw(lambda: bx.get_text("x(t)"))
        by_text = always_redraw(lambda: by.get_text("y(t)"))

        self.play(Write(A_static),Write(B_static))
        self.add(A,B)
        self.remove(A_static,B_static)

        self.play(ShowCreation(bx_static), ShowCreation(by_static), ShowCreation(bx_text_static), ShowCreation(by_text_static))
        self.add(bx,by,bx_text,by_text)
        self.remove(bx_static, by_static, bx_text_static, by_text_static)



        # add vector B.

        # Animate
        self.play(dot_B.animate.move_to(axes.c2p(L * 0.9, 0)), rate_func=there_and_back, run_time=6, )

        # rescale and save the triangle on the sides.
        # Pytagoras and save to the sides.
        # trig and save to the sides.
        # substitute x(t) -> x.
        # define newtonian notation.
        # explain what is we want is ydot.
        # get back pytagoras.
        # derive and go forward
        # we can use cancel notation here that's pretty neat
        self.wait(2)
        pass
