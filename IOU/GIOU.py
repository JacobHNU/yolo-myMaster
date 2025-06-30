import matplotlib.pyplot as plt
import matplotlib.patches as patches
## $$\text{GIoU} = \text{IoU} - \frac{|C - A_{\text{union}}|}{|C|}$$

# 计算GIoU
def calculate_giou(box_a, box_b):
    # 计算IOU部分（左下角，右上角）
    inter_x1 = max(box_a[0], box_b[0])
    inter_y1 = max(box_a[1], box_b[1])
    inter_x2 = min(box_a[2], box_b[2])
    inter_y2 = min(box_a[3], box_b[3])

    # 计算交集面积
    inter_w = max(0, inter_x2 - inter_x1)
    inter_h = max(0, inter_y2 - inter_y1)
    area_inter = inter_w * inter_h

    # 计算并集面积
    area_a = (box_a[2]-box_a[0]) * (box_a[3]-box_a[1])
    area_b = (box_b[2]-box_b[0]) * (box_b[3]-box_b[1])
    area_union = area_a + area_b - area_inter

    #避免除数为0
    if area_union == 0:
        return 0
    # 计算IoU
    iou = area_inter / area_union

    #计算最小闭合区域c
    c_x1 = min(box_a[0], box_b[0])
    c_x2 = max(box_a[2], box_b[2])
    c_y1 = min(box_a[1], box_b[1])
    c_y2 = max(box_a[3], box_b[3])
    area_c = (c_x2 - c_x1) * (c_y2 - c_y1)

    # 计算GIoU,避免除数为0
    if area_c == 0:
        return 0
    giou = iou - (area_c - area_union) / area_c
    # 返回C框坐标，GIoU
    return (c_x1, c_y1, c_x2, c_y2), giou 

def plot_boxes_giou(box_a, box_b):
    fig, ax = plt.subplots(figsize=(6, 6), dpi=150)
    # 绘制原始框
    # 绘制第一个框
    rect_a = patches.Rectangle((box_a[0], box_a[1]), box_a[2]-box_a[0], box_a[3]-box_a[1], linewidth=1, edgecolor='r', facecolor='red',label='Box A', alpha=1.0)
    ax.add_patch(rect_a)
    # 绘制第二个框
    rect_b = patches.Rectangle((box_b[0], box_b[1]), box_b[2]-box_b[0], box_b[3]-box_b[1], linewidth=1, edgecolor='b', facecolor='green', label='Box B', alpha=1.0)
    ax.add_patch(rect_b)

    #计算giou并获取c框
    c_box, giou = calculate_giou(box_a, box_b)
    print("GIoU:", giou)

    # 绘制C框
    rect_c = patches.Rectangle((c_box[0], c_box[1]), c_box[2]-c_box[0], c_box[3]-c_box[1], linewidth=1, edgecolor='g', facecolor='pink', label='Enclosing Box C',alpha=0.5)
    ax.add_patch(rect_c)

    # 设置坐标轴范围
    ax.set_xlim(min(box_a[0], box_b[0]) - 1, max(box_a[2], box_b[2]) + 1)
    ax.set_ylim(min(box_a[1], box_b[1]) - 1, max(box_a[3], box_b[3]) + 1)
    ax.set_title("GIoU: {:.4f}".format(giou)) # 设置标题,保留4位小数
    ax.set_aspect('equal') # 设置坐标轴比例
    ax.legend() # 添加图例
    plt.show()

# 示例用法
box1 = [0, 0, 4, 4]
box2 = [2, 2, 6, 6]
plot_boxes_giou(box1, box2)

