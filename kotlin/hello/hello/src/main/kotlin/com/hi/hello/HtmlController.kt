package com.hi.hello

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable

@Controller
class HtmlController {

    @RequestMapping("/")
    fun index(model:Model):String {
        model.addAttribute("title", "Home")
        return "index"
    }

//  @GetMapping("/post/{num}")
//  fun post(model:Model, @PathVariable num: Int){
//      println("num:\t${num}")
//  }

    @GetMapping("/{formType}")
    fun htmlForm(model:Model, @PathVariable formType:String):String {
        var response : String=""
        if (formType.equals("sign")) {
            response="sign"
        }
        else if (formType.equals("login")) {
            response="login"
        }
        model.addAttribute("title", response)
        return response
    }


//  @GetMapping("/login")
//  fun htmlForm2(model:Model):String {
//      return "login"
//  }
}
