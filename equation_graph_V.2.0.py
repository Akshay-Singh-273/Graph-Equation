#Modules used-------------------------------------

from math import *
from graphics import *

#variable Declaration-----------------------------

org_eqn = {}
rearr_eqn = []
mod_eqn = [0]
answer = []
graph_points = [0]*11
circle = []
line = []
x = 0

winx = 800
winy = 581

yaxis_gap = 20
xaxis_gap = 40
H_gap = 50
xaxis_mid = 301

#function Declarations----------------------------
class equation_solver:
    org_eqn
    type_changed_eqn = []
    rearranged_eqn = []
    coeff_multi_eqn = []
    mul_div_eqn = [1]
    
    def __init__(self, equation):
        self.org_eqn = equation
    
    def operator_counter(self, equation):
        print("\nCounting values to calculate...")
        total_counter = 0
        op_num = 1
        mnd_counter = 0
        for values in equation:
            if values == '+' or values == '-' or values == '/' or values == '*':
                total_counter += 1
            if values == '/' or values == '*':
                mnd_counter += 1
            print("current counter at:",total_counter)
        op_num = total_counter + 1
        memory_needed = op_num - mnd_counter + 1
        return op_num, memory_needed

    def display_list(self, equation):
        for val in equation:
            print(val)

    def change_type(self):
        print("\nChangetype function in progress...")
        r=0
        for o in self.org_eqn:
            try:
                a = int(self.org_eqn[r])
                self.type_changed_eqn.insert(r,a)
            except:
                self.type_changed_eqn.insert(r,self.org_eqn[r])
            r+=1
        print("Changetype function ended...")

    def rearrange(self):
        print("\nRearrange function in progress...")
        arr_counter = None
        for val in self.type_changed_eqn:
            print("Val:",val)
            if arr_counter is None:
                arr_counter = 0
                self.rearranged_eqn.insert(arr_counter, val)
            else:
                if type(val) is int:
                    print("Arr_Counter:",arr_counter)
                    if type(self.rearranged_eqn[arr_counter]) is int:
                        self.rearranged_eqn[arr_counter] = self.rearranged_eqn[arr_counter] * 10 + val
                    else:
                        arr_counter += 1
                        self.rearranged_eqn.append(val)
                elif val == 'c' or val == 'o' or val == 's' or val == 'i' or val == 'n' or val == 't' or val == 'a':
                    if self.rearranged_eqn[arr_counter] == '+' or self.rearranged_eqn[arr_counter] == '-' or self.rearranged_eqn[arr_counter] == '/' or self.rearranged_eqn[arr_counter] == '*':
                        arr_counter += 1
                        self.rearranged_eqn.append(val)
                    else:
                        self.rearranged_eqn[arr_counter] += val
                else:
                    arr_counter += 1
                    self.rearranged_eqn.append(val)
        print("Rearrange function ended...")

    def coeff_multiplier(self, equation, x_value):
        print("Coeff_multi function in progress...")
        operator_num, memory_needed = self.operator_counter(equation)
        coeff_multi_eqn = [1]*(operator_num)
        eqn_counter = 0
        for val in equation:
            print("Val:",val)
            if val == '+' or val == '-' or val == '/' or val == '*':
                eqn_counter += 1
            else:
                if val == 'x':
                    coeff_multi_eqn[eqn_counter] *= x_value
                else:
                    coeff_multi_eqn[eqn_counter] *= val
            print("coeff_eqn[",eqn_counter,"]:",coeff_multi_eqn[eqn_counter])
        print("Coeff_multi function ended...")
        return coeff_multi_eqn

    def multiplication_division(self):
        eqn_counter = 0
        flag = 0
        skip = 0
        last_opr = 0
        final_counter = 0
        operator_num, memory_needed = self.operator_counter(self.rearranged_eqn)
        self.mul_div_eqn = [1]*(memory_needed)
        self.display_list(self.mul_div_eqn)
        print("Multi_divide function in progress...")
        for operator in self.rearranged_eqn:
            if skip == 0:
                print("eqn_counter:",eqn_counter)
                print("final_counter:",final_counter)
                if operator == '/':
                    print("operator found:",operator)
                    last_opr = 0
                    try:
                        self.mul_div_eqn[final_counter] = self.coeff_multi_eqn[eqn_counter] / self.coeff_multi_eqn[eqn_counter+1]
                        print("Value at [",final_counter,"]:",self.mul_div_eqn[final_counter])
                        eqn_counter += 2
                        final_counter += 1
                        skip = 2
                    except:
                        print("Division not possible!")
                        flag = 1
                        break
                elif operator == '*':
                    print("operator found:",operator)
                    self.mul_div_eqn[final_counter] = self.coeff_multi_eqn[eqn_counter] * self.coeff_multi_eqn[eqn_counter+1]
                    print("Value at [",final_counter,"]:",self.mul_div_eqn[final_counter])
                    eqn_counter += 2
                    final_counter += 1
                    skip = 1
                    last_opr = 0
                elif operator == '+' or operator == '-':
                    print("operator found:",operator)
                    last_opr = 1
                    self.mul_div_eqn[final_counter] = self.coeff_multi_eqn[eqn_counter]
                    print("Value at [",final_counter,"]:",self.mul_div_eqn[final_counter])
                    eqn_counter += 1
                    final_counter += 1
                else:
                    continue
            else:
                skip -= 1
                print("skipped")
                continue
        if (eqn_counter == 0 and final_counter == 0) or last_opr == 1:
            self.mul_div_eqn[final_counter] = self.coeff_multi_eqn[eqn_counter]        
        print("Multi_divide function ended...")
        return flag

    def addition_subtraction(self):
        answer = self.mul_div_eqn[0]
        val_counter = 1
        for operator in self.rearranged_eqn:
            if operator == '+':
                answer += self.mul_div_eqn[val_counter]
                val_counter += 1
            elif operator == '-':
                answer -= self.mul_div_eqn[val_counter]
                val_counter += 1
            else:
                continue
        return answer

    def trigonometric(self, rearranged_eqn_cpy, x_value):
        print("Trigno_functions in progress...")
        print("Displaying eqn before modifications:")
        self.display_list(rearranged_eqn_cpy)
        print("Taking x as:",x_value)
        i = 0
        counter = len(rearranged_eqn_cpy) - 1
        for value in rearranged_eqn_cpy:
            print("Value at [",i,"]:",value)
            if value == 'cos':
                rearranged_eqn_cpy.pop(i)
                rearranged_eqn_cpy.pop(i)
                r = i
                while rearranged_eqn_cpy[r] != ')':
                    r += 1
                rearranged_eqn_cpy[i] = self.coeff_multiplier(rearranged_eqn_cpy[i:r], x_value)
                print("Value at [",i,"]:",rearranged_eqn_cpy[i][0])
                rearranged_eqn_cpy[i] = cos(rearranged_eqn_cpy[i][0])
                i += 1
                while r >= i:
                    rearranged_eqn_cpy.pop(i)
                    r -= 1
            elif value == 'sin':
                rearranged_eqn_cpy.pop(i)
                rearranged_eqn_cpy.pop(i)
                r = i
                while rearranged_eqn_cpy[r] != ')':
                    r += 1
                rearranged_eqn_cpy[i] = self.coeff_multiplier(rearranged_eqn_cpy[i:r], x_value)
                print("Value at [",i,"]:",rearranged_eqn_cpy[i][0])
                rearranged_eqn_cpy[i] = sin(rearranged_eqn_cpy[i][0])
                i += 1
                while r >= i:
                    rearranged_eqn_cpy.pop(i)
                    r -= 1
            elif value == 'tan':
                rearranged_eqn_cpy.pop(i)
                rearranged_eqn_cpy.pop(i)
                r = i
                while rearranged_eqn_cpy[r] != ')':
                    r += 1
                rearranged_eqn_cpy[i] = self.coeff_multiplier(rearranged_eqn_cpy[i:r], x_value)
                print("Value at [",i,"]:",rearranged_eqn_cpy[i][0])
                rearranged_eqn_cpy[i] = tan(rearranged_eqn_cpy[i][0])
                i += 1
                while r >= i:
                    rearranged_eqn_cpy.pop(i)
                    r -= 1
            else:
                i += 1
                continue
        print("Trigno_function ended...")

class graph_maker:
    xaxis_marking = []
    gap_diff = 0
    y_coord = []
    graph_points = []
    circle = []
    def __init__(self, equation):
        self.point_eqn = equation

    def grid_maker(self):
        self.point_maker()
        winx = len(self.graph_points)*20
        win = GraphWin("Graph of given equation:", winx , winy)
        X_axis = Line(Point(30, xaxis_mid),Point(winx - 30, xaxis_mid))
        X_axis.draw(win)
        counter = 0
        self.gap_diff = (winx-20)/(len(self.graph_points))
        gap = self.gap_diff+10
        while gap < winx-20:
            self.xaxis_marking.append(Line(Point(gap, xaxis_mid - 5),Point(gap, xaxis_mid + 5)))
            self.xaxis_marking[counter].draw(win)
            counter += 1
            gap += self.gap_diff
        self.point_plotter(win)
       
        
    def point_maker(self):
        try:
            point_eqn = self.point_eqn.remove(None)
            maximum = max(point_eqn)
            minimum = min(point_eqn)
        except:
            maximum = max(self.point_eqn)
            minimum = min(self.point_eqn)
        counter = 0
        avg = (sum(self.point_eqn)/len(self.point_eqn))
        if avg < 0:
            avg *= -1
        print("average:",avg)
        for val in self.point_eqn:
            self.graph_points.append(val / avg)
            counter += 1
        print("Graph_points:")
        for points in self.graph_points:
            print(points)

    def point_plotter(self, win):
        y_coord = 0
        counter = 0
        gap = self.gap_diff
        while counter < len(self.graph_points):
            if(self.graph_points[counter] is None):
                counter += 1
                continue
            else:
                if self.graph_points[counter] <= 0:
                    self.y_coord.append(xaxis_mid + self.graph_points[counter]*(-40))
                else:
                    self.y_coord.append(xaxis_mid - self.graph_points[counter]*(40))
                circle1 = Circle(Point(gap,self.y_coord[counter]),2)
                circle1.setFill("red")
                circle.append(circle1)
                gap += self.gap_diff
                counter += 1
        counter = 0
        skip = 0
        gap = self.gap_diff
        for points in self.point_eqn:
            if(skip == 0):
                try:
                    if(self.point_eqn[counter + 1] == None):
                        skip = 2
                except:
                    continue
                else:
                    line1 = Line(Point(gap, self.y_coord[counter]),Point(gap + self.gap_diff, self.y_coord[counter+1]))
                    line1.setOutline("green")
                    line.append(line1)
                    counter += 1
                    gap += self.gap_diff
            else:
                skip -= 1
        i = 0
        while i<len(circle):
            try:
                line[i].draw(win)
            except:
                i += 1
                continue
            circle[i].draw(win)
            i += 1
        win.getMouse()
        win.close()

#Calling and interface----------------------------
eqn1 = equation_solver(input("Enter the equation(example: 22x+cos(5x)): "))
x_start = int(input("Enter starting value of x: "))
x_end = int(input("Enter end value of x: "))
step_size = float(input("Enter step size: "))
eqn1.change_type()
eqn1.display_list(eqn1.type_changed_eqn)
eqn1.rearrange()
print("rearranged equation:")
eqn1.display_list(eqn1.rearranged_eqn)
ans_index = 0
x = x_start
while x<=x_end:
    rearranged_eqn_cpy = eqn1.rearranged_eqn[:]
    print("-"*50)
    eqn1.trigonometric(rearranged_eqn_cpy , x)
    eqn1.coeff_multi_eqn = eqn1.coeff_multiplier(rearranged_eqn_cpy, x)
    print("Simplified equation(before applying operations):")
    eqn1.display_list(eqn1.coeff_multi_eqn)
    flag = eqn1.multiplication_division()
    if flag == 1:
        answer.append(None)
    else:
        print("Simplified equation(after applying operations):")
        eqn1.display_list(eqn1.mul_div_eqn)
        answer.append(eqn1.addition_subtraction())
    print("-"*50)
    print("FINAL ANSWER TAKING X=",x,":",answer[ans_index])
    print("-"*60)
    x+=step_size
    ans_index += 1
x = x_start
print("For given equation:",eqn1.org_eqn)
r = 0
while x<=x_end:
    print("*"*50)
    print("FINAL ANSWER TAKING X=",x,":",answer[r])
    r+=1
    x+=step_size
input()
#Making Graph-------------------------------------
if(len(answer) != 1):
    graph_obj = graph_maker(answer)
    graph_obj.grid_maker()
