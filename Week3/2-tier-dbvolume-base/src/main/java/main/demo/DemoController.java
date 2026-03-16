package com.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Base64;

@RestController
public class DemoController {

    @GetMapping("/api/config")
    public String config() {

        String app = System.getenv("APP_NAME");
        String env = System.getenv("ENVIRONMENT");
        String msg = System.getenv("APP_MESSAGE");
        String pass = System.getenv("DB_PASSWORD");
        String pod = System.getenv("HOSTNAME");

        String encodedPass = Base64.getEncoder().encodeToString(pass.getBytes());

        return "{"
                + "\"application\":\"" + app + "\","
                + "\"environment\":\"" + env + "\","
                + "\"message\":\"" + msg + "\","
                + "\"password\":\"" + encodedPass + "\","
                + "\"pod\":\"" + pod + "\""
                + "}";
    }
}
