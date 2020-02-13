# COVID-19-Command-Line-Tool
支持自定义要查看的地区.

## 使用的第三方API与库：

[DXY-2019-nCoV-Crawler](https://github.com/BlankerL/DXY-2019-nCoV-Crawler)

PrettyTable


## 数据来源：

疫情数据：[丁香园](https://3g.dxy.cn/newh5/view/pneumonia)

更新时间数据：GitHub项目[DXY-2019-nCoV-Crawler](https://github.com/BlankerL/DXY-2019-nCoV-Crawler)的[OverallAPI](https://lab.isaaclin.cn/nCoV/api/overall)

## 使用方式：

直接终端运行.py文件即可。若要自定义地区请打开.py文件，参照注释对匹配数据进行修改

### 系统要求：

Python版本3.6及以上。

### 依赖库：

re, requests, prettytable, datetime.

### 效果展示：

![image](https://github.com/Lang-Zhou/2019-nCov-Command-Line-Tool/blob/master/sample.png)
(测试环境：macOS 10.15.3, Terminal.app)

### 出错处理

程序已设定API获取数据最大延时为10秒，若运行时报错则大概率为接口问题，请检查网络环境或耐心等待。

## 鸣谢

[DXY-2019-nCoV-Crawler](https://github.com/BlankerL/DXY-2019-nCoV-Crawler)项目发起者提供的API

## 声明

本程序为新型冠状病毒丁香园实时数据爬虫，仅获取距用户运行本程序时刻最近的一次丁香园数据，不存储历史数据.获取到的数据除最近更新时间外，其余全部数据所有权归丁香园所有，且仅做个人了解当前情况之用，若需用于其他目的，请自行联系丁香园获取授权.

本程序出于公益目的，若产生违背本声明的使用所导致的版权纠纷，程序作者不负任何责任。

本程序遵循MIT开源许可.若需在其它项目中使用本程序，请在项目中声明引用.

程序作者是爬虫初学者，其中存在的诸多不足之处，欢迎各位提起issue或邮件联系.
