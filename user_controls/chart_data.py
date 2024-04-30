import flet as ft

class AdhData:
    def __init__(self, expected_datapoints, actual_datapoints, x_fontsize=8, y_fontsize=8, x_range=range(1,8), y_range=range(0,11)):
        self.x_fontsize = x_fontsize
        self.y_fontsize = y_fontsize
        self.x_labels = []
        self.y_labels = []
        self.exp_data = []
        self.act_data = []

        i = 0
        for data_point in expected_datapoints:
            self.exp_data.append(ft.LineChartDataPoint(i+1,data_point))
            i += 1
        
        i = 0
        for data_point in actual_datapoints:
            self.act_data.append(ft.LineChartDataPoint(i+1,data_point))
            i += 1
        
        self.adherance_data = [
            ft.LineChartData(
                data_points=self.exp_data,
                stroke_width=2,
                stroke_cap_round=True,
                curved=False,
                color="#2e3192",
            ),
            ft.LineChartData(
                data_points=self.act_data,
                stroke_width=2,
                stroke_cap_round=True,
                curved=False,
                color="#0072bc",
            ),
        ]
        
        for i in x_range:
            self.x_labels.append(
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Text(f"Day {i}", size=self.x_fontsize, weight=ft.FontWeight.BOLD),
                )
            )
        
        for i in y_range:
            self.y_labels.append(
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Text(f"{i}", size=self.y_fontsize, weight=ft.FontWeight.BOLD),
                )
            )
        
        
    
