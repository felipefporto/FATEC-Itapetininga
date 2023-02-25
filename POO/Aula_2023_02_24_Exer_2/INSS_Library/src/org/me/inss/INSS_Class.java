
package org.me.inss;
public class INSS_Class {
    private String nome;
    private int cpf;
    private String email;
    private double salario_bruto;
    
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setCPF(int cpf){
        this.cpf = cpf;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public void setSalarioBruto(double salario_bruto){
        this.salario_bruto = salario_bruto;
    }
    
    public String getNome(){
        return nome;
    }
    public int getCPF(){
        return cpf;
    }
    public String getEmail(){
        return email;
    }
    public double getSalarioBruto(){
        return salario_bruto;
    }
    
    public double calculaINSS(double salario_bruto){
        return salario_bruto * 0.09;
    }
    public double calculaSalario_Liquido(double salario_bruto){
        return salario_bruto - (salario_bruto * 0.09);
    }
}
