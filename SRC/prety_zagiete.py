import math
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PRETY ZAGIETE")
root.resizable(False, False)

##########################################################################################################################
# FUNKCJE POMOCNICZE:

def oblicz():
    try:
        STECKER_1L.config(text=f"STECKER 1.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get()))  ) /10)}cm")
        STECKER_2L.config(text=f"STECKER 2.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get())) - (int(PR_1LG.get()) * 1.15) - (int(PR_1LD.get()) * 1.15)  ) /10)}cm")
        STECKER_3L.config(text=f"STECKER 3.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get())) - (int(PR_1LG.get()) * 1.15) - (int(PR_1LD.get()) * 1.15) - (int(PR_2LG.get()) * 1.15) - (int(PR_2LD.get()) * 1.15)  ) /10)}cm")
        STECKER_4L.config(text=f"STECKER 4.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get())) - (int(PR_1LG.get()) * 1.15) - (int(PR_1LD.get()) * 1.15) - (int(PR_2LG.get()) * 1.15) - (int(PR_2LD.get()) * 1.15) - (int(PR_3LG.get()) * 1.15) - (int(PR_3LD.get()) * 1.15)  ) /10)}cm")
        S_HAK.config(text=f"S-HAKI: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get()))  ) /10)}cm")
        ABSTANDHALTER_4L_4L.config(text=f"ABSTANDHALTER 4.L - 4.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get())) - (int(PR_1LG.get()) * 1.15) - (int(PR_1LD.get()) * 1.15) - (int(PR_2LG.get()) * 1.15) - (int(PR_2LD.get()) * 1.15) - (int(PR_3LG.get()) * 1.15) - (int(PR_3LD.get()) * 1.15) - (int(PR_4LG.get()) * 1.15) - (int(PR_4LD.get()) * 1.15)  ) /10)}cm")
        ABSTANDHALTER_4L_2L.config(text=f"ABSTANDHALTER 4.L - 2.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get())) - (int(PR_1LG.get()) * 1.15) - (int(PR_1LD.get()) * 1.15) - (int(PR_2LG.get()) * 1.15) - (int(PR_2LD.get()) * 1.15) - (int(PR_3LG.get()) * 1.15) - (int(PR_4LG.get()) * 1.15)  ) /10)}cm")
        ABSTANDHALTER_2L_2L.config(text=f"ABSTANDHALTER 2.L - 2.L: {int((  (int(GR_SB1.get())) - (int(OG_SB1.get())) - (int(OD_SB1.get())) - (int(PR_1LG.get()) * 1.15) - (int(PR_1LD.get()) * 1.15) - (int(PR_2LG.get()) * 1.15) - (int(PR_2LD.get()) * 1.15)  ) /10)}cm")
        UMBUGELUNG.config(text=f"UMBUGELUNG: { math.ceil((  (float(ROZ_PR_PIO_SB1.get())) + (float(ROZ_PR_PIO_SB1.get())) + (float(PR_2LD.get()) * 1.15) + (float(SR_UBL.get()) * 1.15) + (float(SR_UBL.get()) * 1.15)  ) /10)}cm")
        ROZST_S_HAKOW.config(text=f"ROZSTAW S-HAKOW: {int((  (int(ROZ_PR_POZ_SB1.get())) * 4 ) /10)} - {int((  (int(ROZ_PR_PIO_SB1.get())) * 3 ) /10)}")
        ROZST_ABST.config(text=f"ROZSTAW ABSTANDHALTEROW: {(int((  (int(ROZ_PR_POZ_SB1.get())) * 4 ) /10)*2)} - {(int((  (int(ROZ_PR_PIO_SB1.get())) * 3 ) /10)*2)}")
        ROZST_UMBUGELUNGOW.config(text=f"ROZSTAW UMBUGELUNGOW: {int((  (int(ROZ_PR_PIO_SB1.get())) * 3 ) /10)} - 20")

    except ValueError:
        STECKER_1L.config(text=f" - ")
        STECKER_2L.config(text=f" - ")
        STECKER_3L.config(text=f" - ")
        STECKER_4L.config(text=f" - ")
        S_HAK.config(text=f" - ")
        ABSTANDHALTER_4L_4L.config(text=f" - ")
        ABSTANDHALTER_4L_2L.config(text=f" - ")
        ABSTANDHALTER_2L_2L.config(text=f" - ")
        UMBUGELUNG.config(text=f" - ")
        ROZST_S_HAKOW.config(text=f" - ")
        ROZST_ABST.config(text=f" - ")
        ROZST_UMBUGELUNGOW.config(text=f" - ")

##########################################################################################################################
# ELEMENTY POMOCNICZE:       

przycisk_oblicz = ttk.Button(root, text="Oblicz", command=oblicz)
przycisk_oblicz.grid(row=20, columnspan=3, sticky="NSEW")

STECKER_1L = Label(root, justify="left", text=" - ")
STECKER_1L.grid(row=21, columnspan=3, sticky="w")

STECKER_2L = Label(root, justify="left", text=" - ")
STECKER_2L.grid(row=22, columnspan=3, sticky="w")

STECKER_3L = Label(root, justify="left", text=" - ")
STECKER_3L.grid(row=23, columnspan=3, sticky="w")

STECKER_4L = Label(root, justify="left", text=" - ")
STECKER_4L.grid(row=24, columnspan=3, sticky="w")

ODSTEP_1 = Label(root, justify="left", text=" ")
ODSTEP_1.grid(row=25, columnspan=3, sticky="w")

S_HAK = Label(root, justify="left", text=" - ")
S_HAK.grid(row=26, columnspan=3, sticky="w")

ODSTEP_2 = Label(root, justify="left", text=" ")
ODSTEP_2.grid(row=27, columnspan=3, sticky="w")

ABSTANDHALTER_4L_4L = Label(root, justify="left", text=" - ")
ABSTANDHALTER_4L_4L.grid(row=28, columnspan=3, sticky="w")

ABSTANDHALTER_4L_2L = Label(root, justify="left", text=" - ")
ABSTANDHALTER_4L_2L.grid(row=29, columnspan=3, sticky="w")

ABSTANDHALTER_2L_2L = Label(root, justify="left", text=" - ")
ABSTANDHALTER_2L_2L.grid(row=30, columnspan=3, sticky="w")

ODSTEP_3 = Label(root, justify="left", text=" ")
ODSTEP_3.grid(row=31, columnspan=3, sticky="w")

UMBUGELUNG = Label(root, justify="left", text=" - ")
UMBUGELUNG.grid(row=32, columnspan=3, sticky="w")

ODSTEP_4 = Label(root, justify="left", text=" ")
ODSTEP_4.grid(row=33, columnspan=3, sticky="w")

ROZST_S_HAKOW = Label(root, justify="left", text=" - ")
ROZST_S_HAKOW.grid(row=34, columnspan=3, sticky="w")

ROZST_ABST = Label(root, justify="left", text=" - ")
ROZST_ABST.grid(row=35, columnspan=3, sticky="w")

ROZST_UMBUGELUNGOW = Label(root, justify="left", text=" - ")
ROZST_UMBUGELUNGOW.grid(row=36, columnspan=3, sticky="w")

##########################################################################################################################
# GRUBOSC ELEMENTU:

GR_OP1 = Label(root, justify="right", text = "Grubosc elementu [mm]:")
GR_OP1.grid(row = 0, column = 0, sticky="e")

GR_SB1_VAR = StringVar(root)
GR_SB1_VAR.set("1200")
GR_SB1 = ttk.Spinbox(root, from_=0, to=5000, increment=1, width=5, textvariable=GR_SB1_VAR)
GR_SB1.grid(row = 0, column = 1)

ODSTEP_5 = Label(root, justify="left", text=" ")
ODSTEP_5.grid(row=1, columnspan=3, sticky="w")

##########################################################################################################################
# OTULINA GORNA:

OG_OP1 = Label(root, justify="right", text = "Otulina [mm]:")
OG_OP1.grid(row = 2, column = 0, sticky="e")

OG_SB1_VAR = StringVar(root)
OG_SB1_VAR.set("60")
OG_SB1 = ttk.Spinbox(root, from_=0, to=100, increment=1, width=5, textvariable=OG_SB1_VAR)
OG_SB1.grid(row = 2, column = 1)

OG_SCH = Label(root, text = "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯", font=("Arial", 12))
OG_SCH.grid(row = 2, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 1. LAGA GORNA

PR_1LG_OP1 = Label(root, justify="right", text = "1.L [ø]:")
PR_1LG_OP1.grid(row = 3, column = 0, sticky="e")

PR_1LG_VAR = StringVar(root)
PR_1LG_VAR.set("28")
PR_1LG = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_1LG_VAR)
PR_1LG.grid(row = 3, column = 1)

PR_1LG_SCH = Label(root, text = "█████████████", font=("Arial", 12))
PR_1LG_SCH.grid(row = 3, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 2. LAGA GORNA

PR_2LG_OP1 = Label(root, justify="right", text = "2.L [ø]:")
PR_2LG_OP1.grid(row = 4, column = 0, sticky="e")

PR_2LG_VAR = StringVar(root)
PR_2LG_VAR.set("28")
PR_2LG = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_2LG_VAR)
PR_2LG.grid(row = 4, column = 1)

PR_2LG_SCH = Label(root, text = "⬤      ⬤      ⬤      ⬤", font=("Arial", 12))
PR_2LG_SCH.grid(row = 4, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 3. LAGA GORNA

PR_3LG_OP1 = Label(root, justify="right", text = "3.L [ø]:")
PR_3LG_OP1.grid(row = 5, column = 0, sticky="e")

PR_3LG_VAR = StringVar(root)
PR_3LG_VAR.set("28")
PR_3LG = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_3LG_VAR)
PR_3LG.grid(row = 5, column = 1)

PR_3LG_SCH = Label(root, text = "█████████████", font=("Arial", 12))
PR_3LG_SCH.grid(row = 5, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 4. LAGA GORNA

PR_4LG_OP1 = Label(root, justify="right", text = "4.L [ø]:")
PR_4LG_OP1.grid(row = 6, column = 0, sticky="e")

PR_4LG_VAR = StringVar(root)
PR_4LG_VAR.set("28")
PR_4LG = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_4LG_VAR)
PR_4LG.grid(row = 6, column = 1)

PR_4LG_SCH = Label(root, text = "⬤      ⬤      ⬤      ⬤", font=("Arial", 12))
PR_4LG_SCH.grid(row = 6, column = 2)

##########################################################################################################################
# SRODEK PRZEKROJU

SR_PRZ_OP1 = Label(root, justify="right", text = " ")
SR_PRZ_OP1.grid(row = 7, column = 0, sticky="e")

##########################################################################################################################
# PRETY ZBROJENIOWE - 4. LAGA DOLNA

PR_4LD_OP1 = Label(root, justify="right", text = "4.L [ø]:")
PR_4LD_OP1.grid(row = 8, column = 0, sticky="e")

PR_4LD_VAR = StringVar(root)
PR_4LD_VAR.set("28")
PR_4LD = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_4LD_VAR)
PR_4LD.grid(row = 8, column = 1)

PR_4LD_SCH = Label(root, text = "⬤      ⬤      ⬤      ⬤", font=("Arial", 12))
PR_4LD_SCH.grid(row = 8, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 3. LAGA DOLNA

PR_3LD_OP1 = Label(root, justify="right", text = "3.L [ø]:")
PR_3LD_OP1.grid(row = 9, column = 0, sticky="e")

PR_3LD_VAR = StringVar(root)
PR_3LD_VAR.set("28")
PR_3LD = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_3LD_VAR)
PR_3LD.grid(row = 9, column = 1)

PR_3LD_SCH = Label(root, text = "█████████████", font=("Arial", 12))
PR_3LD_SCH.grid(row = 9, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 2. LAGA DOLNA

PR_2LD_OP1 = Label(root, justify="right", text = "2.L [ø]:")
PR_2LD_OP1.grid(row = 10, column = 0, sticky="e")

PR_2LD_VAR = StringVar(root)
PR_2LD_VAR.set("28")
PR_2LD = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_2LD_VAR)
PR_2LD.grid(row = 10, column = 1)

PR_2LD_SCH = Label(root, text = "⬤      ⬤      ⬤      ⬤", font=("Arial", 12))
PR_2LD_SCH.grid(row = 10, column = 2)

##########################################################################################################################
# PRETY ZBROJENIOWE - 1. LAGA DOLNA

PR_1LD_OP1 = Label(root, justify="right", text = "1.L [ø]:")
PR_1LD_OP1.grid(row = 11, column = 0, sticky="e")

PR_1LD_VAR = StringVar(root)
PR_1LD_VAR.set("28")
PR_1LD = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=PR_1LD_VAR)
PR_1LD.grid(row = 11, column = 1)

PR_1LD_SCH = Label(root, text = "█████████████", font=("Arial", 12))
PR_1LD_SCH.grid(row = 11, column = 2)

##########################################################################################################################
# OTULINA DOLNA:

OD_OP1 = Label(root, justify="right", text = "Otulina [mm]:")
OD_OP1.grid(row = 12, column = 0, sticky="e")

OD_SB1_VAR = StringVar(root)
OD_SB1_VAR.set("60")
OD_SB1 = ttk.Spinbox(root, from_=0, to=5000, increment=1, width=5, textvariable=OD_SB1_VAR)
OD_SB1.grid(row = 12, column = 1)

OD_SCH = Label(root, text = "________________", font=("Arial", 12))
OD_SCH.grid(row = 12, column = 2)

ODSTEP_6 = Label(root, justify="left", text=" ")
ODSTEP_6.grid(row=13, columnspan=3, sticky="w")

##########################################################################################################################
# POZIOMY ROZSTAW PRETOW:

ROZ_PR_POZ_OP1 = Label(root, justify="right", text = "Poziomy rozstaw pretow [mm]:")
ROZ_PR_POZ_OP1.grid(row = 14, column = 0, sticky="e")

ROZ_PR_POZ_SB1_VAR = StringVar(root)
ROZ_PR_POZ_SB1_VAR.set("125")
ROZ_PR_POZ_SB1 = ttk.Spinbox(root, from_=0, to=1000, increment=1, width=5, textvariable=ROZ_PR_POZ_SB1_VAR)
ROZ_PR_POZ_SB1.grid(row = 14, column = 1)

##########################################################################################################################
# PIONOWY ROZSTAW PRETOW:

ROZ_PR_PIO_OP1 = Label(root, justify="right", text = "Pionowy rozstaw pretow [mm]:")
ROZ_PR_PIO_OP1.grid(row = 15, column = 0, sticky="e")

ROZ_PR_PIO_SB1_VAR = StringVar(root)
ROZ_PR_PIO_SB1_VAR.set("150")
ROZ_PR_PIO_SB1 = ttk.Spinbox(root, from_=0, to=1000, increment=1, width=5, textvariable=ROZ_PR_PIO_SB1_VAR)
ROZ_PR_PIO_SB1.grid(row = 15, column = 1)

ODSTEP_7 = Label(root, justify="left", text=" ")
ODSTEP_7.grid(row=16, columnspan=3, sticky="w")

##########################################################################################################################
# SREDNICA UMBUGELUNGOW:

SR_UBL_OP1 = Label(root, justify="right", text = "Srednica Umbugelungow [ø]:")
SR_UBL_OP1.grid(row = 17, column = 0, sticky="e")

SR_UBL_VAR = StringVar(root)
SR_UBL_VAR.set("16")
SR_UBL = ttk.Spinbox(root, from_=6, to=50, increment=1, width=5, textvariable=SR_UBL_VAR)
SR_UBL.grid(row = 17, column = 1)


root.mainloop()