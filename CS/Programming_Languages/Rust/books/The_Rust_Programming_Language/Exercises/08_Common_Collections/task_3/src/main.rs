// Using a hash map and vectors, create a text interface to allow a user to add employee names
// to a department in a company. For example, “Add Sally to Engineering” or “Add Amir to Sales.”
// Then let the user retrieve a list of all people in a department or all people in the company
// by department, sorted alphabetically.

use std::collections::HashMap;

fn add_department(company: &mut HashMap<String, Vec<String>>, department_name: String) {
    let mut dep: Vec<String> = Vec::new();
    let dep_name = &department_name.clone();
    company.entry(department_name).or_insert(dep);
    println!("Department '{0}' has been added to the company.", dep_name);
}

fn add_employee_to_department(
    company: &mut HashMap<String, Vec<String>>,
    department_name: String,
    person_name: String,
) {
    let dep: Option<&mut Vec<String>> = company.get_mut(&department_name);
    match dep {
        Some(d) => d.push(person_name),
        _ => println!(
            "There is no department '{0}' in the company. Add this departmnent first.",
            &department_name
        ),
    }
}

fn get_department_emploees(
    company: &mut HashMap<String, Vec<String>>,
    department_name: String,
) -> Option<&Vec<String>> {
    let dep: Option<&Vec<String>> = company.get(&department_name);
    match dep {
        Some(d) => Some(d),
        _ => {
            println!(
                "There is no department '{0}' in the company.\n",
                &department_name
            );
            None
        }
    }
}


fn main() {
    let mut company: HashMap<String, Vec<String>> = HashMap::new();
    let engineering = "Engineering".to_string();
    let sales = "Sales".to_string();
    
    add_department(&mut company, "Sales".to_string());
    add_employee_to_department(&mut company, sales.clone(), "Sally".to_string());
    add_employee_to_department(&mut company, engineering.clone(), "John".to_string());
    add_department(&mut company, engineering.clone());
    add_employee_to_department(&mut company, engineering.clone(), "John".to_string());
    add_employee_to_department(&mut company, engineering.clone(), "Mark".to_string());
    println!("{company:#?}");
    
    
    let empl_dep: Option<&Vec<String>> = get_department_emploees(&mut company, engineering.clone());
    if let Some(dep) = empl_dep {
        println!("Department 'Engineering':\n{dep:#?}\n")
    }
    
    let empl_dep: Option<&Vec<String>> = get_department_emploees(&mut company, "Any department".to_string());
    if let Some(dep) = empl_dep {
        println!("Department 'Any department':\n{dep:#?}\n")
    } 
}
