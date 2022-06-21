# Check_In
### 文件说明

- moyupai.py 保存了[摸鱼派](https://pwl.icu/)网站自动签到脚本
- muacloud.py 保存了[muacloud](https://muacloud.cloud/)网站自动签到脚本
- gamekegs.py 保存了[gamekegs](https://gamekegs.com/)网站自动签到脚本
- juejin.py 保存了[掘金](https://juejin.cn/)网站自动签到脚本
- 91.py保存了[91tvg](https://www.91tvg.com/)网站自动签到脚本

### 使用方法

fork本项目后，在Settings->Secrets中新建仓库密码（New repository secret），根据你需要执行的签到脚本进行添加。例如你想对摸鱼派网站进行每日自动签到，则添加name为`MOYUPAI_USERNAME`，value为你摸鱼派登录的账户邮箱或者用户名，另外继续添加name为`MOYUPAI_PASSWORD`，value为你摸鱼派登录的密码，如下图所示

![](https://z3.ax1x.com/2021/10/12/5mKENV.png#shadow)

![](https://z3.ax1x.com/2021/10/12/5mKxV1.png#shadow)

另外，我在Github Actions中默认配置了摸鱼派、掘金、游戏大桶、muacloud四个网站的签到脚本，但是大家不一定全部都要用，具体来说，你想签到什么网站，修改`.github/workflows/main.yml`文件即可，如下图所示

![](https://z3.ax1x.com/2021/10/13/5uIr2d.png#shadow)

### v1.1 版本更新

去掉代码中冗余的`time.sleep()`，改为使用`driver.implicitly_wait(10)`隐式等待所有操作10s，并且通过`@retry`修饰函数，使其报错后重新执行，增加鲁棒性，避免网络波动等因素的影响导致签到失败

### v1.2版本更新

现在不需要手动上传chromedriver，也不需要每次手动更新chromedriver，main.yaml脚本支持自动获取最新的chromedriver文件

### 参考项目

- [掘金滑动拼图验证码识别](https://github.com/shuai93/juejin)
- [图片验证码ocr](https://github.com/sml2h3/ddddocr)
