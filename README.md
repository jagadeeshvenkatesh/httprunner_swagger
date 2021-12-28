@[toc] 使用手册请参考最后说明！

@[author] wx:oupoor

@[swagger] 仅支持swagger2.0版本，3.0部分数据存在解析错误

#### 背景介绍
```
鉴于大多数互联网公司均采用java作为后台开发语言，且习惯使用Swagger插件生成接口文档；
本项目的开发，是为解决测试人员依赖swagger接口文档做接口测试需要cv/cp的重复手工劳动。
```
#### 项目需求
- 为什么要做接口测试？
```
受自动化测试分层思想影响：UI自动化投入/维护成本高且收益甚微，
而当下测试人员编码能力有限，那么中间层的接口测试战略位置尤为重要；
1、更快实现接口自动化测试，更早加入持续集成；
2、通过定制触发器实时监控生产应用服务健康状况；
3、后端服务的性能测试更是需要掌握接口测试的基础。
```
- 如何开展接口测试？
```
首先需要了解主流接口协议，如http，明白接口组成以及请求和响应过程；
再者需要知道接口测试的业务范围，前端的功能测试与之并不是重复工作；
最后需要清楚业务规则及接口的业务逻辑实现，才能更好的服务接口测试。
```
- 如何才能减去反复的手工活动？
> 做接口测试时，需要组装接口url及入参，对着接口文档和接口测试工具无限制的ctrl+c / ctrl+v？

```
首推自动化测试技术!

推荐接口测试工具：jmeter/httprunner/postman/rf，不排除其他框架，它们都能向往着DDT的方向发展;
接口测试工具原理：都是通过脚本/工具实现模拟客户端向服务端发起请求，然后校验服务器返回数据的过程。
```
#### 实现一
```
python编写脚本对swagger2.x接口文档返回的josn数据对象进行解析，提取接口信息，
按规则写入excel组成测试用例，支持excel转成csv结合jmeter实现DDT接口自动化测试；

2021-08-05，使用pandas模块将生成xlsx用例文件转成csv文件
```
#### 实现二
```
引入httprunner<2.x>框架，同样是通过解析swagger2.x接口文档生成的json格式的数据文件；
<亦可通过charles抓包工具导出har文件，再通过har2case转换json测试用例>，可以直接通过CLI执行；
```
`本项目不包含httprunner框架，需要用户自己安装：pip install httprunner==2.4.3`

#### 实现三
```
既然已知swagger接口文档并且能解析数据形成excel或者json格式的测试用例，
那么也可以结合python/java等开发语言集合单元测试框架搭建自动化测试框架。
```
#### 项目结构说明：
- logs：存放脚本执行日志
- properties：存放配置信息
- swagger：存放生成json测试用例文件
- swaggerLib：解析swagger接口文档脚本，包含一个testsuite脚本生成的用例格式可与httprunnermanager批量导入有效
- utils：封装工具包
- common：
- - dir_config.py：为项目拼接路径配置模块

### 使用说明
- 本地安装python开发环境
- 克隆项目到本地：git clone
- 安装项目依赖:pip install -r requirements.txt
- 因为项目中swagger.py脚本已经引用了dir_config工程结构，会先创建目录对应目录
- 确认config.ini配置文件需要解析的接口文档地址
- 执行程序入口在swagger脚本main代码块，也可以使用单独抽取出来放在项目根路径
- SwaggerTestSuites生成json格式数据是给httprunnermanager这个项目批量导入接口使用的