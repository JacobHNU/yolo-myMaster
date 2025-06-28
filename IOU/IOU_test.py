import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_iou(box_a, box_b):
    # 计算交集坐标
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

    # 避免除零错误
    return area_inter / area_union if area_union > 0 else 0

def plot_boxes(box_a, box_b):
    fig, ax = plt.subplots()
    # 绘制第一个框
    rect_a = patches.Rectangle((box_a[0], box_a[1]), box_a[2]-box_a[0], box_a[3]-box_a[1], linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect_a)
    # 绘制第二个框
    rect_b = patches.Rectangle((box_b[0], box_b[1]), box_b[2]-box_b[0], box_b[3]-box_b[1], linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(rect_b)

    # 设置坐标轴范围
    ax.set_xlim(min(box_a[0], box_b[0]) - 1, max(box_a[2], box_b[2]) + 1)
    ax.set_ylim(min(box_a[1], box_b[1]) - 1, max(box_a[3], box_b[3]) + 1)
    ax.set_aspect('equal')
    plt.show()

box1 = [0, 0, 4, 4]
box2 = [2, 2, 6, 6]
iou = calculate_iou(box1, box2)

# 绘制框并返回iou值
plot_boxes(box1, box2)
print(iou)
# IoU: 0.14285714285714285