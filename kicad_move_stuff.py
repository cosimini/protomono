from kipy import KiCad
from kipy.geometry import Vector2, Angle

def get_selection_ids():
    elems = []
    for e in KiCad().get_board().get_selection():
        elems.append(e.reference_field.text.value)
    return elems

# RIGHT HAND
P_R = ['CH14', 'CH26', 'CH1', 'CH13', 'CH2']
A_R = ['CH15', 'CH27', 'CH49', 'CH3']
M_R = ['CH28', 'CH37', 'CH16', 'CH4']
I_R = ['CH6', 'CH30', 'CH17', 'CH29', 'CH5', 'CH18', 'CH42', 'CH41']
T_R = ['CH40', 'CH38', 'CH39']
# LEFT HAND
P_L = ['CH12', 'CH11', 'CH35', 'CH24', 'CH23']
A_L = ['CH10', 'CH22', 'CH34', 'CH50']
M_L = ['CH21', 'CH33', 'CH44', 'CH9']
I_L = ['CH43', 'CH20', 'CH31', 'CH32', 'CH7', 'CH48', 'CH19', 'CH8']
T_L = ['CH47', 'CH46', 'CH45']

if __name__=='__main__':
    try:
        kicad = KiCad()
        print(f"Connected to KiCad {kicad.get_version()}")
    except BaseException as e:
        print(f"Not connected to KiCad: {e}")
        exit(1)
    board = kicad.get_board()
    footprints = board.get_footprints()
    for f in footprints:
        if f.reference_field.text.value == "D1":
            #f.position += Vector2.from_xy_mm(5, 2)
            f.orientation += Angle.from_degrees(90)
            board.update_items(f)

