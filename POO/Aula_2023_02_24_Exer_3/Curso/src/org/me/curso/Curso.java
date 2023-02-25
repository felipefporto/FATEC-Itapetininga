
package org.me.curso;

public class Curso {
    private String Nome;
    private int Duracao;
    private double Valor;
    
    public Curso(String nome, int duracao, double valor){
        this.Nome = nome;
        this.Duracao = duracao;
        this.Valor = valor;
        
    }
    
    public void setNome(String nome){
        this.Nome = nome;
    }
    
    public String getNome(){
        return Nome;
    }
    public int getDuracao(){
        return Duracao;
    }
    public double getValor(){
        return Valor;
    }
    
    
}
