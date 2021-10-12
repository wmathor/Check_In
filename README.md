# Check_In
### 文件说明

- moyupai.py 保存了[摸鱼派](https://pwl.icu/)网站自动签到脚本
- muacloud.py 保存了[muacloud](https://muacloud.cloud/)网站自动签到脚本
- gamekegs.py 保存了[gamekegs](https://gamekegs.com/)网站自动签到脚本

### 使用方法

fork本项目后，在Settings->Secrets中新建仓库密码（New repository secret），根据你需要执行的签到脚本进行添加。例如你想对摸鱼派网站进行每日自动签到，则添加name为`MOYUPAI_USERNAME`，value为你摸鱼派登录的账户邮箱或者用户名，另外继续添加name为`MOYUPAI_PASSWORD`，value为你摸鱼派登录的密码，如下图所示

![](https://z3.ax1x.com/2021/10/12/5mKENV.png#shadow)

![](https://z3.ax1x.com/2021/10/12/5mKxV1.png#shadow)

### 参考项目

- [掘金滑动拼图验证码识别](https://github.com/shuai93/juejin)
- [图片验证码ocr](https://github.com/sml2h3/ddddocr)
