from manimlib import *
import numpy as np


class Test(Scene):
    def construct(self):
        eq1 = Tex(r"{{a^2}} + {{b^2}} = {{c^2}}")
        eq2 = Tex(r"({{a^2}})' + {{b^2}} = {{c^2}} {{\dot{x}}}")
        self.add(eq1)
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.play(eq2.animate.shift(DOWN))
        self.wait(0.5)

        self.wait(10)
        pass


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

        axes = Axes(# x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(0, 6, 2), # y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(0, 6, 2), # The axes will be stretched so as to match the specified
            # height and width
            height=6, width=6, # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={"stroke_color": GREY_A, "stroke_width": 1, }, # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={"include_tip": False, }, x_axis_config={"include_tip": False, })
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )

        # Create axes and move intro

        self.play(Write(axes, lag_ratio=0.01, run_time=1), intro.animate.shift(3 * UP))

        # write point A then point B then create a line between them. Add always redraw on Dot_A and we fix this shit!
        L = 5
        x = 3
        # dot_A = always_redraw(lambda: Dot(color=Yellow).move_to(axes.c2p(0,np.sqrt(25-x**2))))
        dot_A = Dot(color=Yellow).move_to(axes.c2p(0, np.sqrt(L ** 2 - x ** 2)))
        dot_B = Dot(color=Blue).move_to(axes.c2p(x, 0))
        line = Line(dot_A, dot_B, color=RED)

        # Braces
        # by = always_redraw(Brace,Line(dot_A.get_center(),axes.c2p(0,0)),1.4*LEFT)
        # bx = always_redraw(Brace,Line(dot_B.get_center(),axes.c2p(0,0)),1.4*DOWN)
        # xtext, xnumber = xlabel = VGroup(Text("x(t) = "), DecimalNumber(0, show_ellipsis=True, num_decimal_places=2, include_sign=True, ))
        # ytext, ynumber = ylabel = VGroup(Text("y(t) = "), DecimalNumber(0, show_ellipsis=True, num_decimal_places=2, include_sign=True, ))
        # xlabel.add_updater(lambda m: m.next_to(bx, DOWN))
        # ylabel.add_updater(lambda m: m.next_to(by, LEFT))

        self.play(FadeIn(dot_A), scale=0.5)
        self.wait()
        self.play(FadeIn(dot_B))
        self.wait()
        self.play(Write(line))

        line_update = always_redraw(lambda: Line(dot_A, dot_B, color=RED))
        self.add(line_update)
        self.play(FadeOut(line))

        # Change rate function by doing MoveAlongPath() and defining Lines for vertical and horizontal
        dot_origin = Dot().move_to(axes.c2p(0, 0))
        new_x = 0
        linex = always_redraw(lambda: Line(Dot().move_to(axes.c2p(new_x, 0)), dot_origin))
        liney = always_redraw(lambda: Line(Dot().move_to(axes.c2p(0, np.sqrt(L ** 2 - new_x ** 2))), dot_origin))
        self.play(MoveAlongPath(dot_B, linex, rate_func=linear), MoveAlongPath(dot_A, liney, rate_func=rush_into))
        new_x = 5
        self.play(MoveAlongPath(dot_B, linex, rate_func=linear), MoveAlongPath(dot_A, liney, rate_func=rush_into))
        new_x = 2
        self.play(MoveAlongPath(dot_B, linex, rate_func=linear), MoveAlongPath(dot_A, liney, rate_func=rush_into))
        self.wait()

        # add labels and brackets to

        # add vector B.
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
