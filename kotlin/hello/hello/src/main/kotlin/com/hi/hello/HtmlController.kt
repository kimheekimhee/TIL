package com.hi.hello

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.ui.Model

@Controller
class HtmlController {

    @RequestMapping("/")
    fun index(model:Model):String {
        return "index"
    }
}
