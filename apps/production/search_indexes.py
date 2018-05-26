# # 定义全文检索类
# from haystack import indexes
#
# from apps.production.models import Carstyle
#
# class carstyleIndex(indexes.SearchIndex,indexes.Indexable):
#     text = indexes.CharField(document=True,use_template=True)
#     def get_model(self):
#         return Carstyle
#     # 返回模型类
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()
#
# #     建立索引数据


from haystack import indexes
# 修改此处，为你自己的model
from apps.production.models import Carstyle
# 修改此处，类名为模型类的名称+Index，比如模型类为GoodsInfo,则这里类名为GoodsInfoIndex
class carstyleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
    # 修改此处，为你自己的model
        return Carstyle
    def index_queryset(self, using=None):
        return self.get_model().objects.all()