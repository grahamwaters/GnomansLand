<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/grahamwaters/GnomansLand">
    <img src="../images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">GnomansLand</h3>

  <p align="center">
    A simulation God-Mode Game with free will and reinforcement learning!
    <br />
    <a href="https://github.com/grahamwaters/GnomansLand"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/grahamwaters/GnomansLand/issues">Report Bug</a>
    ·
    <a href="https://github.com/grahamwaters/GnomansLand/issues">Request Feature</a>
  </p>
</div>

Feel free to share this repo by Tweeting it!

[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Get%20over%20170%20free%20design%20blocks%20based%20on%20Bootstrap%204&url=https://froala.com/design-blocks&via=froala&hashtags=bootstrap,design,templates,blocks,developers)


## Ideas that could be used later

### Future Work
There is a chance that the agent will forget where it has been and will get "lost". This would occur when the agent's confidence attribute falls below its personality threshold during exploration and a variable "chance" (which ranges from 0 to 1) is greater than 0.95. In this case the agent begins randomly walking from its current position and loses more health than usual. This is not implemented in the base simulation but in a more advanced version.
