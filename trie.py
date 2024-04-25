from collections import deque
import copy

##############################################################################################
# Trie是一颗前缀树，应用与多级分类情况：
#
# 电磁学  静电场及其应用  库仑定律
# 电磁学  静电场及其应用  电荷
# 电磁学  电路及其应用	  串联电路和并联电路	电表的改装
# 力学    运动的描述      质点   
# 力学    运动的描述      质点
# 力学	  运动的描述      时间和位移
# 力学	  相互作用        重力                重力的概念
# 力学	  相互作用        弹力
#
##############################################################################################

class TrieNode(object):
    def __init__(self):
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    # labels 相当于每一行标签，category是每一个标签
    # 注意：从左到右层级是一级，二级，三级，...
    def insert(self, labels):
        current = self.root
        for category in labels:
            if category not in current.children:
                current.children[category] = TrieNode()
            current = current.children[category]

    # 返回最顶层层级与列表
    def top(self):
        if not self.root:
            return (0,[])
        result = []
        for category in self.root.children.keys():
            result.append(category)
        return (1,result)

    # 返回所在级别的下一级层级与列表
    def next(self, labels):
        level, result = 1, []
        if not self.root:
            return (0,[])
        
        current = self.root
        for category in labels:
            if category not in current.children:
                return (0,[])
            current = current.children[category]
            level = level + 1
        
        if current.children and len(current.children) > 0:
            for category in current.children.keys():
                result.append(category)
            return (level,result)
        else:
            return (0, [])
    
    # 层序遍历，并返回所有的层级
    def level_order(self):
        if not self.root:
            return [[]]
        
        queue = deque()
        
        # 把顶层放入进去，同时也要把前面的路径放入进去
        top_level = []
        for category in self.root.children.keys():
            # 元组，前面是当前标签依赖路径，后面是当前的标签
            category_comopose = ([], category)
            top_level.append(category_comopose)

        # 顶层放入队列
        queue.append(top_level)

        result = []
        while queue:
            level_list = queue.popleft()
            level_category = []
            next_comopose = []
            for category_comopose in level_list:
                labels, category = category_comopose
                # 保存当前的列表
                level_category.append(category)

                labels_copy = copy.deepcopy(labels)
                labels_copy.append(category)
                (level, tags) = self.next(labels_copy)
                if self.check_level(level) and len(tags) > 0:
                    for tag in tags:
                        next_comopose.append((labels_copy, tag))
            # 保存当前层级所有的组合
            if len(next_comopose) > 0:
                next_comopose_copy = copy.deepcopy(next_comopose)
                queue.append(next_comopose_copy)
            
            # 保存当前层级列表
            if len(level_category) > 0:
                result.append(level_category)
        
        return result

def get_txt_tags(file_name):
    
    with open(file_name, "r") as fp:
        lines = fp.readlines()

    trie = Trie()
    for line in lines:
        line = line.strip()
        line_list = line.split("\t")
        line_list.pop(0)
        #print(line_list)
        trie.insert(line_list)
   
    print(trie.top())
    print(trie.next(["电磁学"]))
    print(trie.next(["电磁学","静电场及其应用"]))
    
    # 层序遍历
    result = trie.level_order()
    for level in result:
        print(len(level),level)

if __name__=="__main__":
    get_txt_tags("./category.txt")
