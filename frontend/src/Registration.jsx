import React, { useState } from 'react'
import { Box, TextField, Button } from "@material-ui/core"
import { Redirect, Link } from "react-router-dom"

export default function Registration({ submit }) {
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [phone, setPhone] = useState("")
    const [password, setPassword] = useState("")
    const handleChangeEmail = (event) => {
        setEmail(event.target.value)
    }
    const handleChangePassword = (event) => {
        setPassword(event.target.value)
    }
    const handleChangePhone = (event) => {
        setPhone(event.target.value)
    }
    const handleChangeName = (event) => {
        setName(event.target.value)
    }

    return (
        <Box sx={{ height: "100%", width: "100%", alignItems: "center", display: "flex", justifyContent: "center", flexDirection: "column" }}>
            <TextField
                type="text"
                label="ФИО"
                value={name}
                onChange={handleChangeName}
            />
            <TextField
                type="email"
                label="Email"
                value={email}
                onChange={handleChangeEmail}
            />
            
            <TextField
                type="tel"
                label="Номер телефона"
                value={phone}
                onChange={handleChangePhone}
                style={{ marginTop: 5 }}
            />

            <TextField
                type="password"
                label="Пароль"
                value={password}
                onChange={handleChangePassword}
                style={{ marginTop: 5 }}
            />

            <Button variant="outlined" color="primary" style={{ marginTop: 10 }} onClick={() => {
                console.log(typeof submit)
                submit()()
            }}>Забронировать</Button>

        </Box>
    )
}
