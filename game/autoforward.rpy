default m_stored_position = []
default s_stored_position = []
default n_stored_position = []
default y_stored_position = []

default m_stored_position_no_data = False
default s_stored_position_no_data = False
default n_stored_position_no_data = False
default y_stored_position_no_data = False

init python:
    
    
    
    
    def getposition(poshash):
        if poshash == [t11]:
            return "t11"
        elif poshash == [i11]:
            return "t11"
        elif poshash == [s11]:
            return "t11"
        elif poshash == [h11]:
            return "t11"
        elif poshash == [d11]:
            return "t11"
        elif poshash == [l11]:
            return "t11"
        elif poshash == [r11]:
            return "t11"
        
        elif poshash == [lf11]:
            return "f11"
        elif poshash == [rf11]:
            return "f11"
        elif poshash == [hf11]:
            return "f11"
        elif poshash == [f11]:
            return "f11"
        
        elif poshash == [t21]:
            return "t21"
        elif poshash == [i21]:
            return "t21"
        elif poshash == [s21]:
            return "t21"
        elif poshash == [h21]:
            return "t21"
        elif poshash == [d21]:
            return "t21"
        elif poshash == [l21]:
            return "t21"
        elif poshash == [r21]:
            return "t21"
        
        elif poshash == [lf21]:
            return "f21"
        elif poshash == [rf21]:
            return "f21"
        elif poshash == [hf21]:
            return "f21"
        elif poshash == [f21]:
            return "f21"
        
        elif poshash == [t22]:
            return "t22"
        elif poshash == [i22]:
            return "t22"
        elif poshash == [s22]:
            return "t22"
        elif poshash == [h22]:
            return "t22"
        elif poshash == [d22]:
            return "t22"
        elif poshash == [l22]:
            return "t22"
        elif poshash == [r22]:
            return "t22"
        
        elif poshash == [lf22]:
            return "f22"
        elif poshash == [rf22]:
            return "f22"
        elif poshash == [hf22]:
            return "f22"
        elif poshash == [f22]:
            return "f22"
        
        elif poshash == [t31]:
            return "t31"
        elif poshash == [i31]:
            return "t31"
        elif poshash == [s31]:
            return "t31"
        elif poshash == [h31]:
            return "t31"
        elif poshash == [d31]:
            return "t31"
        elif poshash == [l31]:
            return "t31"
        elif poshash == [r31]:
            return "t31"
        
        elif poshash == [lf31]:
            return "f31"
        elif poshash == [rf31]:
            return "f31"
        elif poshash == [hf31]:
            return "f31"
        elif poshash == [f31]:
            return "f31"
        
        elif poshash == [t32]:
            return "t32"
        elif poshash == [i32]:
            return "t32"
        elif poshash == [s32]:
            return "t32"
        elif poshash == [h32]:
            return "t32"
        elif poshash == [d32]:
            return "t32"
        elif poshash == [l32]:
            return "t32"
        elif poshash == [r32]:
            return "t32"
        
        elif poshash == [lf32]:
            return "f32"
        elif poshash == [rf32]:
            return "f32"
        elif poshash == [hf32]:
            return "f32"
        elif poshash == [f32]:
            return "f32"
        
        elif poshash == [t33]:
            return "t33"
        elif poshash == [i33]:
            return "t33"
        elif poshash == [s33]:
            return "t33"
        elif poshash == [h33]:
            return "t33"
        elif poshash == [d33]:
            return "t33"
        elif poshash == [l33]:
            return "t33"
        elif poshash == [r33]:
            return "t33"
        
        elif poshash == [lf33]:
            return "f33"
        elif poshash == [rf33]:
            return "f33"
        elif poshash == [hf33]:
            return "f33"
        elif poshash == [f33]:
            return "f33"
        
        elif poshash == [t41]:
            return "t41"
        elif poshash == [i41]:
            return "t41"
        elif poshash == [s41]:
            return "t41"
        elif poshash == [h41]:
            return "t41"
        elif poshash == [d41]:
            return "t41"
        elif poshash == [l41]:
            return "t41"
        elif poshash == [r41]:
            return "t41"
        
        elif poshash == [lf41]:
            return "f41"
        elif poshash == [rf41]:
            return "f41"
        elif poshash == [hf41]:
            return "f41"
        elif poshash == [f41]:
            return "f41"
        
        elif poshash == [t42]:
            return "t42"
        elif poshash == [i42]:
            return "t42"
        elif poshash == [s42]:
            return "t42"
        elif poshash == [h42]:
            return "t42"
        elif poshash == [d42]:
            return "t42"
        elif poshash == [l42]:
            return "t42"
        elif poshash == [r42]:
            return "t42"
        
        elif poshash == [lf42]:
            return "f42"
        elif poshash == [rf42]:
            return "f42"
        elif poshash == [hf42]:
            return "f42"
        elif poshash == [f42]:
            return "f42"
        
        elif poshash == [t43]:
            return "t43"
        elif poshash == [i43]:
            return "t43"
        elif poshash == [s43]:
            return "t43"
        elif poshash == [h43]:
            return "t43"
        elif poshash == [d43]:
            return "t43"
        elif poshash == [l43]:
            return "t43"
        elif poshash == [r43]:
            return "t43"
        
        elif poshash == [lf43]:
            return "f43"
        elif poshash == [rf43]:
            return "f43"
        elif poshash == [hf43]:
            return "f43"
        elif poshash == [f43]:
            return "f43"
        
        elif poshash == [t44]:
            return "t44"
        elif poshash == [i44]:
            return "t44"
        elif poshash == [s44]:
            return "t44"
        elif poshash == [h44]:
            return "t44"
        elif poshash == [d44]:
            return "t44"
        elif poshash == [l44]:
            return "t44"
        elif poshash == [r44]:
            return "t44"
        
        elif poshash == [lf44]:
            return "f44"
        elif poshash == [rf44]:
            return "f44"
        elif poshash == [hf44]:
            return "f44"
        elif poshash == [f44]:
            return "f44"
        
        #This is the "Dumbass, you just fed it one of the weird-ass special transforms that you shouldn't be running this autofocus script with" transform that should make it *really damn obvious* when it's fed a transform that it can't handle:
        else:
            return "kaiju"
        #When this eventually gets released to others, I want to release it with this warning message instead of the "kaiju" thing, since it makes more sense than giving them that weird-ass transform.
        #else:
        #    renpy.call_screen("dialog","ERROR:\nTransform or position not recognized.\nPlease ensure position tag is properly defined in autofocus script.", ok_action=Return())
    
    
    
    def monika_focus_2(event, interact=True, **kwargs):
        global m_stored_position
        global m_stored_position_no_data
        
        
        if event == "begin":
            initial_pos = renpy.get_at_list("monika")
            if initial_pos == []:
                if not m_stored_position:
                    renpy.call_screen("dialog","ERROR:\nMonika has no current pose and no stored pose.\nAutofocus will not work for her correctly.", ok_action=Return())
                    m_stored_position_no_data = True
                else:
                    initial_pos = m_stored_position
                    renpy.show("monika", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
                    m_stored_position_no_data = False
            else:
                m_stored_position = renpy.get_at_list("monika")
                renpy.show("monika", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
        if event == "show" and not m_stored_position_no_data:
            if renpy.get_at_list("monika") == []:
                pass
            elif m_stored_position <> renpy.get_at_list("monika"):
                m_stored_position = getposition(renpy.get_at_list("monika"))
        if event == "end" and not m_stored_position_no_data:
            if renpy.get_at_list("monika") == []:
                renpy.show("monika", at_list=[wherepos[getposition(m_stored_position)]], zorder=1)
                m_stored_position_no_data = False
            else:
                renpy.show("monika", at_list=[wherepos[getposition(renpy.get_at_list("monika"))]], zorder=1)
                m_stored_position = renpy.get_at_list("monika")
                m_stored_position_no_data = False
        elif event == "end" and m_stored_position_no_data:
            m_stored_position_no_data = False
    
    def sayori_focus_2(event, interact=True, **kwargs):
        global s_stored_position
        global s_stored_position_no_data
        
        
        if event == "begin":
            initial_pos = renpy.get_at_list("sayori")
            if initial_pos == []:
                if not s_stored_position:
                    renpy.call_screen("dialog","ERROR:\nSayori has no current pose and no stored pose.\nAutofocus will not work for her correctly.", ok_action=Return())
                    s_stored_position_no_data = True
                else:
                    initial_pos = s_stored_position
                    renpy.show("sayori", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
                    s_stored_position_no_data = False
            else:
                s_stored_position = renpy.get_at_list("sayori")
                renpy.show("sayori", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
        if event == "show" and not s_stored_position_no_data:
            if renpy.get_at_list("sayori") == []:
                pass
            elif s_stored_position <> renpy.get_at_list("sayori"):
                s_stored_position = getposition(renpy.get_at_list("sayori"))
        if event == "end" and not s_stored_position_no_data:
            if renpy.get_at_list("sayori") == []:
                renpy.show("sayori", at_list=[wherepos[getposition(s_stored_position)]], zorder=1)
                s_stored_position_no_data = False
            else:
                renpy.show("sayori", at_list=[wherepos[getposition(renpy.get_at_list("sayori"))]], zorder=1)
                s_stored_position = renpy.get_at_list("sayori")
                s_stored_position_no_data = False
        elif event == "end" and s_stored_position_no_data:
            s_stored_position_no_data = False
    
    def natsuki_focus_2(event, interact=True, **kwargs):
        global n_stored_position
        global n_stored_position_no_data
        
        
        if event == "begin":
            initial_pos = renpy.get_at_list("natsuki")
            if initial_pos == []:
                if not n_stored_position:
                    renpy.call_screen("dialog","ERROR:\nNatsuki has no current pose and no stored pose.\nAutofocus will not work for her correctly.", ok_action=Return())
                    n_stored_position_no_data = True
                else:
                    initial_pos = n_stored_position
                    renpy.show("natsuki", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
                    n_stored_position_no_data = False
            else:
                n_stored_position = renpy.get_at_list("natsuki")
                renpy.show("natsuki", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
        if event == "show" and not n_stored_position_no_data:
            if renpy.get_at_list("natsuki") == []:
                pass
            elif n_stored_position <> renpy.get_at_list("natsuki"):
                n_stored_position = getposition(renpy.get_at_list("natsuki"))
        if event == "end" and not n_stored_position_no_data:
            if renpy.get_at_list("natsuki") == []:
                renpy.show("natsuki", at_list=[wherepos[getposition(n_stored_position)]], zorder=1)
                n_stored_position_no_data = False
            else:
                renpy.show("natsuki", at_list=[wherepos[getposition(renpy.get_at_list("natsuki"))]], zorder=1)
                n_stored_position = renpy.get_at_list("natsuki")
                n_stored_position_no_data = False
        elif event == "end" and n_stored_position_no_data:
            n_stored_position_no_data = False
    
    def yuri_focus_2(event, interact=True, **kwargs):
        global y_stored_position
        global y_stored_position_no_data
        
        
        if event == "begin":
            initial_pos = renpy.get_at_list("yuri")
            if initial_pos == []:
                if not y_stored_position:
                    renpy.call_screen("dialog","ERROR:\nYuri has no current pose and no stored pose.\nAutofocus will not work for her correctly.", ok_action=Return())
                    y_stored_position_no_data = True
                else:
                    initial_pos = y_stored_position
                    renpy.show("yuri", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
                    y_stored_position_no_data = False
            else:
                y_stored_position = renpy.get_at_list("yuri")
                renpy.show("yuri", at_list=[wherepos[getposition(initial_pos)]], zorder=3)
        if event == "show" and not y_stored_position_no_data:
            if renpy.get_at_list("yuri") == []:
                pass
            elif y_stored_position <> renpy.get_at_list("yuri"):
                y_stored_position = getposition(renpy.get_at_list("yuri"))
        if event == "end" and not y_stored_position_no_data:
            if renpy.get_at_list("yuri") == []:
                renpy.show("yuri", at_list=[wherepos[getposition(y_stored_position)]], zorder=1)
                y_stored_position_no_data = False
            else:
                renpy.show("yuri", at_list=[wherepos[getposition(renpy.get_at_list("yuri"))]], zorder=1)
                y_stored_position = renpy.get_at_list("yuri")
                y_stored_position_no_data = False
        elif event == "end" and y_stored_position_no_data:
            y_stored_position_no_data = False
    
    def mpos(m_position_override):
        global m_stored_position
        m_stored_position = m_position_override
        return
    
    def spos(s_position_override):
        global s_stored_position
        s_stored_position = s_position_override
        return
    
    def npos(n_position_override):
        global n_stored_position
        n_stored_position = n_position_override
        return
    
    def ypos(y_position_override):
        global y_stored_position
        y_stored_position = y_position_override
        return
    
    def auto_pos(m_manual,s_manual,n_manual,y_manual):
        if m_manual and renpy.get_at_list("monika"):
            mpos(m_manual)
        if s_manual and renpy.get_at_list("sayori"):
            spos(s_manual)
        if n_manual and renpy.get_at_list("natsuki"):
            npos(n_manual)
        if y_manual and renpy.get_at_list("yuri"):
            ypos(y_manual)



label autofocus_start():
    #Applying automatic leans towards the front...
    $ m.display_args["callback"] = monika_focus_2
    $ s.display_args["callback"] = sayori_focus_2
    $ n.display_args["callback"] = natsuki_focus_2
    $ y.display_args["callback"] = yuri_focus_2
    
    python:
        wherepos = {
            "t11" : f11,
            "f11" : t11,
            
            "t21" : f21,
            "t22" : f22,
            "f21" : t21,
            "f22" : t22,
            
            "t31" : f31,
            "t32" : f32,
            "t33" : f33,
            "f31" : t31,
            "f32" : t32,
            "f33" : t33,
            
            "t41" : f41,
            "t42" : f42,
            "t43" : f43,
            "t44" : f44,
            "f41" : t41,
            "f42" : t42,
            "f43" : t43,
            "f44" : t44,
            
            "kaiju" : kaiju
        }
    return
    
label autofocus_end():
    #Applying automatic leans towards the front...
    $ s.display_args["callback"] = None
    $ y.display_args["callback"] = None
    $ n.display_args["callback"] = None
    $ m.display_args["callback"] = None
    
    $ m_stored_position = []
    $ s_stored_position = []
    $ n_stored_position = []
    $ y_stored_position = []
    
    $ m_stored_position_no_data = False
    $ s_stored_position_no_data = False
    $ n_stored_position_no_data = False
    $ y_stored_position_no_data = False
    
    return


label afw:
    
    $ renpy.watch(renpy.get_at_list("monika"))
    $ renpy.watch(m_stored_position)
    $ renpy.watch(renpy.get_at_list("sayori"))
    $ renpy.watch(s_stored_position)
    $ renpy.watch(renpy.get_at_list("natsuki"))
    $ renpy.watch(n_stored_position)
    $ renpy.watch(renpy.get_at_list("yuri"))
    $ renpy.watch(y_stored_position)

    return

label afuw:
    python:
        renpy.unwatch(renpy.get_at_list(monika))
        renpy.unwatch(m_stored_position)
        renpy.unwatch(renpy.get_at_list(sayori))
        renpy.unwatch(s_stored_position)
        renpy.unwatch(renpy.get_at_list(natsuki))
        renpy.unwatch(n_stored_position)
        renpy.unwatch(renpy.get_at_list(yuri))
        renpy.unwatch(y_stored_position)
    
    return