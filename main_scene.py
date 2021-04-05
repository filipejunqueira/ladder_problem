from manimlib import *



class Test(Scene):
    def construct(self):
        intro_text = TexText("Hello")
        intro_text2 = TextText("I deleted everything... :(")
        self.play(ShowCreation(intro_text))
        self.play(ReplacementTransform(intro_text,intro_text2))
        self.wait()

class Cancel(VGroup):
    CONFIG = {
        "line_kwargs": {"color":RED},
        "buff_text": None,
        "buff_line": 0.7,
    }
    def __init__(self,text,texmob=None,**kwargs):
        digest_config(self,kwargs)
        VGroup.__init__(self,**kwargs)

        pre_coord_dl = text.get_corner(DL)
        pre_coord_ur = text.get_corner(UR)
        reference_line = Line(pre_coord_dl,pre_coord_ur)
        reference_unit_vector = reference_line.get_unit_vector()
        coord_dl = text.get_corner(DL) - text.get_center() - reference_unit_vector*self.buff_line
        coord_ur = text.get_corner(UR) - text.get_center() + reference_unit_vector*self.buff_line
        if texmob == None:
            line = Line(coord_dl,coord_ur,**self.line_kwargs)
            self.add(line)
        else:
            arrow = Arrow(coord_dl,coord_ur,**self.line_kwargs)
            unit_vector = arrow.get_unit_vector()
            if self.buff_text == None:
                self.buff_text = get_norm((texmob.get_center()-texmob.get_critical_point(unit_vector))/2)*2
                texmob.move_to(arrow.get_end()+unit_vector*self.buff_text)
                self.add(arrow,texmob)


class CancelTerms(Scene):
    def construct(self):
        formula = TexText("f(x)",height=1)
        cancel_formula = Cancel(formula,Tex("testa"))
        self.add(formula,cancel_formula)
        self.wait(10)


class Introduction(Scene):
    def construct(self):
        pass


class Ladder(Scene):
    def contruct(self):

        # write down axes.
        # write point A then point B then create a line between them.
        # add labels and brackets to.
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




        pass