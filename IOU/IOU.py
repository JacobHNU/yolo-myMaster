import matplotlib.pyplot as plt

def calculate_iou(box_a, box_b):
    # 计算交集坐标
    inter_x1 = max(box_a[0], box_b[0]) # 1, 2
    inter_y1 = min(box_a[1], box_b[1]) # 4, 5
    inter_x2 = min(box_a[2], box_b[2]) # 3, 4
    inter_y2 = max(box_a[3], box_b[3]) # 2, 3

    # 计算交集面积
    inter_w = max(0, inter_x2 - inter_x1)
    inter_h = max(0, inter_y1 - inter_y2) 
    area_inter = inter_w * inter_h

    # 计算并集面积
    area_a = (box_a[2]-box_a[0])*(box_a[1]-box_a[3]) # (x2-x1)*(y2-y1)

    area_b = (box_b[2]-box_b[0])*(box_b[1]-box_b[3]) # (x2-x1)*(y2-y1)
    area_uion = area_a + area_b - area_inter

    # 避免除数为0
    if area_uion == 0:
        return 0

    # 计算IOU
    iou = area_inter / area_uion
    return iou

def plot_box(box_a, box_b):
    fig, ax = plt.subplots() # 创建一个图像
   # 绘制第一个框
    rect_a = plt.Rectangle((box_a[0], box_a[1]+ box_a[3]-box_a[1]), box_a[2]-box_a[0], box_a[1]-box_a[3], linewidth=1, edgecolor='r', facecolor='none') # 绘制矩形 参数表示矩形的左下角坐标（默认）和宽度和高度
    ax.add_patch(rect_a) # 添加矩形到坐标轴
    # 绘制第二个框
    rect_b = plt.Rectangle((box_b[0], box_b[1]+ box_b[3]-box_b[1]), box_b[2]-box_b[0], box_b[1]-box_b[3], linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(rect_b)

    #设置坐标轴范围
    ax.set_xlim(min(box_a[0], box_b[0])-1, max(box_a[2], box_b[2])+1) # 设置x轴范围,加1是为了包含框的边界  
    ax.set_ylim(min(box_a[3], box_b[3])-1, max(box_a[1], box_b[1])+1) 
    ax.set_aspect('equal') # 设置坐标轴比例
    plt.show()

box1=[1,4,3,2]
box2=[2,5,4,3]    

#计算IOU
iou = calculate_iou(box1, box2) 
print(iou) 

#绘制框
plot_box(box1, box2)




























