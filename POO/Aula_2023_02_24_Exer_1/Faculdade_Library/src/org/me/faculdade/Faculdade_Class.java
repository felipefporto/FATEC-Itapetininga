package org.me.faculdade;
public class Faculdade_Class {
    private String nome;
    private String curso;
    private int ra;
    private double nota;
    private double mensalidade;
    
    public void setNome (String nome){
        this.nome = nome;
    }
    public void setCurso (String curso){
        this.curso = curso;
    }
    public void setRA (int ra){
        this.ra = ra;
    }
    public void setNota (double nota){
        this.nota = nota;
    }
    public void setMensalidade (double mensalidade){
        this.mensalidade = mensalidade;
    }
    
    public String getNome(){
        return nome;
    }
    public String getCurso(){
        return curso;
    }
    public int getRA(){
        return ra;
    }
    public double getNota(){
        return nota;
    }
    public double getMensalidade(){
        return mensalidade;
    }
    
    public double calculaDesconto(double mensalidade){
        if (nota >= 9.0) return mensalidade * 0.5;
        return mensalidade;
    } 
}            
